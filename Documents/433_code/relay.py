import socket
import serial
import json
import RPi.GPIO as GPIO
from modules import config
from time import time, sleep
from struct import pack, unpack

GPIO.setmode(GPIO.BCM)

for pin in config.mode_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
GPIO.setup(config.aux_pin, GPIO.IN)
rf_uart = serial.Serial(config.serial_path, config.baud_rate, timeout = config.timeout)
GPIO.output(config.mode_pins[0], 0)
GPIO.output(config.mode_pins[1], 0)



def putRF(op, data=b''):
    """
    FUNCTION: putRF
    ARGS:
        OPCODE = 2 bits 0b00-0b11 represents purpose/mode of message
        DATA = data payload packed using struct.pack
    RETURNS: none
    """
    if(GPIO.input(config.aux_pin)):
        length = len(data)
        length = (length & 0b00111111)
        end_byte = ((op << 6) | length)
        if length > 0:
            rf_uart.write(pack('B', end_byte) + data + pack('B', end_byte))
            rf_uart.flush()
            return len(data)
        else:
            rf_uart.write(pack('B', end_byte) + pack('B', end_byte))
            return 0

    else:
        print("NOT READY")


def getRF():
    op = 0b00
    length = 0b000000
    start_byte = 0
    start_byte = unpack('B', rf_uart.read(1))[0]
    if start_byte == 0:
        return 0
    else:
        op = (start_byte >> 6)
        print(f"OP: {op}")
        length = (start_byte & 0b00111111)
        print(f"Length: {length}")
        if length > 0:
            data = rf_uart.read(length)
            stop_byte = unpack('B', rf_uart.read(1))[0]
            if start_byte == stop_byte:
                print(f"ENDS MATCH:\nOP:{op}\nDATA:{data}")
                return (op, data)
            else:
                print("BAD ENDS")
                return(-1, -1)
        else:
            return (op, 0)

def getSock():
    try:
        while True:
            data, addr = s.recvfrom(128)
            if data:
                return data
    except Exception as e:
        print(f"ERROR: {e}")

def request_gps():
    try:
        putRF(config.gps_op)
        unused_op, packed_gps = getRF()
        location = unpack('2f', packed_gps)
        return location
    except Exception as e:
        print(e)

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 26)
    s.settimeout(5.0)
    s.bind((config.host, config.port))

    while True:
        print("Receiving")
        buf =  getSock()
        if buf:
            print(f"Sending: {buf}")
            putRF(0b00, buf)
            print(len(buf))
