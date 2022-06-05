#!/usr/bin/env python3.5
"""
Sender test script to check communications through ebytes
"""
import socket
import serial
import RPi.GPIO as GPIO
from modules import config
from time import time, sleep
from struct import pack, unpack

# set pins to rx and tx on the ebyte module 
GPIO.setmode(GPIO.BCM)

for pin in config.mode_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
GPIO.setup(config.aux_pin, GPIO.IN)


rf_uart = serial.Serial(config.serial_path, config.baud_rate, timeout=0.1)
GPIO.output(config.mode_pins[0], 0)                    #if the extra pins on the ttl usb are connected to m0 & m1 on the ebyte module
GPIO.output(config.mode_pins[1], 0)                    #then these two lines will send low logic to both which puts the module in transmit mode 0


#receive data from networked socket on the LAN, send over uart to rf module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 26)
s.bind((config.host, config.port))

def getSock():
    try:
        s.listen(1)
        client_socket, addr = s.accept()
        while True:
            data = client_socket.recv(128)
            if data:
                return data
                break
        return data
    except:
        print("Error in getSock()")



def packDEEZNUTZ(): #object to bytes
    # arbiratry values for struct with 7 ints
    try:
        return pack('7i', int(1), int(2), int(3), int(4), int(5), int(6), int(7))

    except:
        print("Error in D")

def unpackGPS(gps):
    # unpack a struct of 2 ints
    return unpack("2i", gps)

def unpackDEEZNUTZ(message): #object to bytes

    #try:
    data = unpack('7i', message)
    print(data)    
    return data
    #except:
    #    print("Error in D")


def putRF(op, data): 
    """
    gets called in loop
    if the aux pin is HIGH, its not busy.

    Get len of data we want to send
    Mask it to first six bits of the start byte

    """
    if(GPIO.input(config.aux_pin)):                          #arguments to make function more self-contained and function-like
        length = len(data)
        length = (length & 0b00111111)
        print(length)
        start_byte, end_byte = ((op << 6) | length) #opcode and length 
        rf_uart.write(pack('B', start_byte) + data + pack('B', end_byte))   #start byte + payload + stop byte
        rf_uart.flush() 
        return len(data)                 #waits until all data is written
    else:
        print("NOT READY")

def getRF():
    """
    get reply from the rover, make sure same data is coming back to ensure the connection works
    """
    op = 0b00
    length = 0b000000
    start_byte = 0
    start_byte = unpack('B', rf_uart.read(1))[0] #wait for byte until timeout
    if start_byte == 0:
        return 0 #if timeout return 0
    else:
        op = (start_byte >> 6)
        print("OP")
        print(op)
#     """
    
#     """
#     try:
#         putRF(GPS_OP) #send just the GPS request OP to rover,
#         # empty data arg defaults to empty string and the function
#         #  will only send the end bytes
#         unused_op, packed_gps = getRF() #gets op code and data returned, data returned will be a packed
#         #struct containing two floats for lat, lon
#         location = unpack('2f', packed_gps)
#         return location #location is a tuple
#     except Exception as e:
#         print(e)
        data = rf_uart.read(length) 
        stop_byte = unpack('B', rf_uart.read(1))[0] #the following byte should be the stop byte
        if start_byte == stop_byte:
            print("ENDS MATCH")
            print(op)
            print(data)
            return (op, data)
        else: #if that last byte wasn't the stop byte then something is out of sync
            print("BAD ENDS")
            return -1




while True:
    

    buf = packDEEZNUTZ()
    print("sending")
    putRF(1, buf)

'''        print("getting")
        rover_gps = getRF(8)
        if rover_gps > 0:
            rover_gps = unpackGPS(rover_gps)
            print("******************************************************************")
            print(rover_gps)
'''    

