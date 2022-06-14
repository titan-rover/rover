import json
import sys
import netifaces as ni
from pathlib import Path


DEFAULT_CONFIG = {
    "MOBILITY_OP": "0b00",
    "GPS_OP": "0b01",
    "TERMINAL_OP": "0b01",
    "GPIO":
        {
            "MODE_PINS": [23, 24],
            "AUX_PIN": 18
        },
    "SERIAL_PATH": "/dev/serial0",
    "BAUD_RATE": 19200,
    "TIMEOUT": 1.0
}


class Config():
    def __init__(self):
        self._config = self.read_config_file()
        self.mobility_op = self._config["MOBILITY_OP"]
        self.gps_op = self._config["GPS_OP"]
        self.terminal_op = self._config["TERMINAL_OP"]
        self.mode_pins = self._config["GPIO"]["MODE_PINS"]
        self.aux_pin = self._config["GPIO"]["AUX_PIN"]
        self.serial_path = self._config["SERIAL_PATH"]
        self.baud_rate = self._config["BAUD_RATE"]
        self.timeout = self._config["TIMEOUT"]
        self.host = self.get_host_address()
        self.port = self._config["PORT"]

    
    def read_config_file(self):
        base_path = str(Path(__file__).resolve().parents[1])
        config_path = base_path+"/config.json"
        try:
            config_file = open(config_path, 'r')
        except FileNotFoundError as e:
                print(f"ERROR: config.json FILE NOT FOUND IN DIRECTORY {base_path}\n GENERATING A NEW ONE AT PATH {config_path}")
                sys.exit(1)

        return json.loads(config_file.read())

    def get_host_address(self):
        """
        Parameters: None
        Returns: Ip address value in ipv4 address notation

        Looks for the value of the "HOST" key in the config.json, if the value is empty double quotes
        use the ip address of the host machine, at the interface 'eth0' (the default ethernet interface for the rpi).
        
        If there is a value for the "HOST" key, use that instead. 
        """
        if self._config["HOST"] == "":
            ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
            return ip
        return self._config["HOST"]

config = Config()
