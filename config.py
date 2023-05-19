import json


def get_filename():
    config_json = 'config.json'
    filename = 'filename'
    with open(config_json, 'r') as f:
        config = json.load(f)
    return config[filename]
