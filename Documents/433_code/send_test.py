import socket
import serial
import datetime 
import sys
from datetime import datetime
from time import time, sleep
from modules import config

with serial.Serial(config.serial_path, 19200, timeout=5) as ser:
    while True:
        x = ser.readline()
        if x:
            print(x.decode())