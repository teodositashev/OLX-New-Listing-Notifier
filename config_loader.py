import os
import yaml

def load_config(filepath='config.yaml'):
    """Load configuration from the YAML file."""
    
    if not os.path.exists(filepath):
        raise FileNotFoundError("The configuration file does not exist.")
    
    try:
        with open(filepath, 'r') as file:
            config = yaml.safe_load(file)
            return config
    except yaml.YAMLError as exc:
        raise RuntimeError(f"Error reading the YAML file: {exc}")