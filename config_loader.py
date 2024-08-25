import os
import re
import yaml
from typing import Any, Dict

EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
GMAIL_REGEX = r'\b[a-zA-Z0-9._%+-]+@gmail\.com$'

def load_config(filepath: str = 'config.yaml') -> Dict[str, Any]:
    """Load configuration from the YAML file."""
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Configuration file '{filepath}' does not exist.")
    
    try:
        with open(filepath, 'r') as file:
            config = yaml.safe_load(file)
            validate_config(config)
            return config
    except yaml.YAMLError as exc:
        raise RuntimeError(f"Error reading the YAML file: {exc}")
    
def validate_config(config: Dict[str, Any]) -> None:
    """Validate the configuration for time interval, email addresses, and search link."""
    
    if (config['time_interval'] < 1):
        raise ValueError("Time interval must be a positive integer.")
    
    if (not is_valid_email(config['sender_email'], GMAIL_REGEX)):
        raise ValueError("Sender email must be a valid Gmail address.")
    
    if (not is_valid_email(config['receiver_email'], EMAIL_REGEX)):
        raise ValueError("Receiver email must be a valid email address.")
    
    if (not config['link'].startswith('https://www.olx.bg')):
        raise ValueError("Provided link must be a valid OLX search query URL.")
    
    config['link'] = ensure_sorted_by_newest(config['link'])

def is_valid_email(email: str, regex: str) -> bool:
    """Check if the given email matches the specified regex pattern."""

    return bool(re.match(regex, email))


def ensure_sorted_by_newest(url: str) -> str:
    """Ensure the OLX search link is sorted by the newest results."""
    
    pattern = r'(&?search%5Border%5D=[^&]*)'
    
    match = re.search(pattern, url)
    
    if match:
        new_url = re.sub(pattern, r'&search%5Border%5D=created_at%3Adesc', url)
    else:
        # If no search[order] parameter exists, add it at the end
        separator = '&' if '?' in url else '?'
        new_url = f"{url}{separator}search%5Border%5D=created_at%3Adesc"
    
    return new_url