import socket
import RPi.GPIO as GPIO
import serial
import traceback
import sys
from time import sleep
from .errors import *
from .config import config
from struct import pack, unpack


class Relay:
    def __init__(self):
        self.serial_connection = self._get_serial_connection()
        self.socket = self._CreateSocket()

    def _get_serial_connection(self):
        """
        Class method for initiating a serial connection using the pyserial Serial() method.
        If serial path is not found, will retry until it is.
        retry_seconds is incremented by 5 each time until reaching 60 seconds. 

        Variables:
            connection: A serial.Serial() object using the information from the config.json values loaded into the config.py object. 

        Returns:
            serial.Serial() connection object 

        Errors:
            Serial_Port_Not_Active_Error: Raises an error that the serial path in config.json cannot be reached, waits for retry_seconds ,increments by 5 up to 60 seconds, then calls the function again 

        """
        retry_seconds = 5
        try:
            connection = serial.Serial(config.serial_path, config.baud_rate, timeout=config.timeout)
            if not connection.is_open():
                raise Serial_Port_Not_Active_Error(config.serial_path, retry_seconds)
            connection.setDTR(True) #if the extra pins on the ttl usb are connected to m0 & m1 on the ebyte module
            connection.setRTS(True) #then these two lines will send low logic to both which puts the module in transmit mod$
            return connection

        except Serial_Port_Not_Active_Error as e:
            print(f"Serial Port Not active: {e}")
            sleep(retry_seconds)
            if retry_seconds <= 60:
                retry_seconds += 5
            self.get_serial_connection(self)

        except Exception as e:
            print(f"Generic exception: {e}")


    def GetRF(self):
        op = config.mobility_op
        length = 0b000000
        start_byte = 0
        start_byte = unpack('B', self.serial_connection.read(1))[0]
        if start_byte == 0:
            return 0
        else:
            op = (start_byte >> 6)
            length = (start_byte & 0b00111111)
            if length > 0:
                data =self.serial_connection.read(length)
                stop_byte = unpack('B', self.serial_connection.read(1))[0]
                if start_byte == stop_byte:
                    return(op, data)
                else:
                    return(-1, -1)
            else:
                return(op, 0)

    def RequestGPS(self):
        try:
            self.PutRF(config.gps_op)
            unused_op, packed_gps = self.GetRF()
            location = unpack('2f', packed_gps)
            return location
        except Exception as e:
            print(f"ERROR: {e}")

    def _CreateSocket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 26)
        s.settimeout(5.0)
        s.bind((config.host, config.port))
        return s

    def GetSock(self):
        try:
            while True:
                data, addr = self.socket.recvfrom(128)
                if data:
                    return data
        except Exception as e:
            print(f"ERROR: {e}")

    def PutRF(self, op, data = b''):
        if(GPIO.input(config.aux_pin)):
            length = len(data)
            length = (length & 0b00111111)
            start_byte, end_byte = ((op << 6) | length)
            if length > 0:
                self.serial_connection.write(pack('B', start_byte) + data + pack('B', end_byte))
                self.serial_connection.flush()
                return len(data)
            else:
                self.serial_connection.write(pack('B', start_byte) + pack('B', end_byte))
                self.serial_connection.flush()
                return 0
        else:
            print(f"Reciever Not Ready...")
