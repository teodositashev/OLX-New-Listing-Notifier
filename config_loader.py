import os
import re
import yaml

EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
GMAIL_REGEX = r'\b[a-zA-Z0-9._%+-]+@gmail\.com$'

def load_config(filepath='config.yaml'):
    """Load configuration from the YAML file."""

    if not os.path.exists(filepath):
        raise FileNotFoundError("The configuration file does not exist.")
    
    try:
        with open(filepath, 'r') as file:
            config = yaml.safe_load(file)
            validate_config(config)
            return config
    except yaml.YAMLError as exc:
        raise RuntimeError(f"Error reading the YAML file: {exc}")
    
def validate_config(config):
    """Validates the config whether we have a valid search query, valid email addresses and time interval."""

    if (config['time_interval'] < 1):
        raise Exception("The time interval needs to be a whole number greater than 0.")
    
    if (validate_email(GMAIL_REGEX, config['sender_email']) == False):
        raise Exception("The sender email needs to be a gmail address.")
    
    if (validate_email(EMAIL_REGEX, config['receiver_email']) == False):
        raise Exception("The receiver email needs to be a valid email address.")
    
    if (config['link'].startswith('https://www.olx.bg/ads/q') == False):
        raise Exception("The provided link needs to be a valid OLX search query.")
    
    config['link'] = ensure_sorted_by_newest(config['link'])

    return config

def validate_email(email, regex):
    if (re.match(regex, email)):
        return True
    return False

def ensure_sorted_by_newest(url):
    pattern = r'(&?search%5Border%5D=[^&]*)'
    
    match = re.search(pattern, url)
    
    if match:
        new_url = re.sub(pattern, r'&search%5Border%5D=created_at%3Adesc', url)
    else:
        # If no search[order] parameter exists, add it at the end
        separator = '&' if '?' in url else '?'
        new_url = f"{url}{separator}search%5Border%5D=created_at%3Adesc"
    
    return new_url