import json
import sys
from pathlib import Path



class Config():
    def __init__(self):
        self._config = self.read_config_file()
        self.ubiquiti_address = self._config["BASESTATION_UBIQUITI_ADDRESS"]
        self.username = self._config["SSH_USERNAME"]
        self.password = self._config["SSH_PASSWORD"]

    
    def read_config_file(self):
        # find out the parent path of config.py
        base_path = str(Path(__file__).resolve().parents[1])
        # assuming the config is in the directory above this .py file, append the config filename to the path
        config_path = base_path+"/config.json"
        try:
            config_file = open(config_path, 'r')
        except FileNotFoundError as e:
                print(f"ERROR: config.json FILE NOT FOUND IN DIRECTORY {base_path}\n GENERATING A NEW ONE AT PATH {config_path}")
                sys.exit(1)
        return json.loads(config_file.read())

config = Config()