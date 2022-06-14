#! /usr/bin/env python2

import rospy, subprocess, sys
from mobility.msg import Status
import serial as ser

telem = Status()
#modes
PAUSE = -1 #LS + B3
IDLE = 0
MOBILITY = 1 #LS + B2
ARM = 2    #LS + B4
TYPER = 3  #LS + B11
BOTH = 4  #R2 + B1
AUTO = 5

def ser_callback(data):
    j5_cmd = data.cmd_msg[0]
    j5_2_cmd = data.cmd_msg[1]
    j4_cmd = data.cmd_msg[2]
    j1_cmd = data.cmd_msg[3]
    #servo1 = data.cmd_msg[4]
    #servo2 = data.cmd_msg[5]
    #solenoid = data.cmd_msg[6]

    if len(j5_cmd) == 0:
        j5_cmd = '3'
    if len(j5_2_cmd) == 0:
        j5_2_cmd = '3'
    if len(j4_cmd) == 0:
        j4_cmd = '3'
    if len(j1_cmd) == 0:
        j1_cmd = '3'
    #if len(servo1) == 0:
    #    servo1 = '3'
    #if len(servo2) == 0:
        #servo2 = '3'
    #if len(solenoid) == 0:
        #solenoid = '3'

    #cmd = [j5_cmd,j5_2_cmd,j4_cmd,j1_cmd,servo1,servo2,solenoid]
    cmd = [j5_cmd,j5_2_cmd,j4_cmd,j1_cmd]
    #print(cmd)
    cmd = bytearray(cmd)
    ser_cmd.write(cmd)
    #ser_cmd.flush()
'''
    feed_test = ser_cmd.read()#read a line
    if len(feed_test) > 4:#pyboard has 12 but ADC 0-4095. len cannot be > 4
        pass
    else:
        #feed_test = int(feed_test)
        print(feed_test)
'''
if __name__ == '__main__':
    rospy.init_node('serial_gernerator',anonymous=True)
    sub = rospy.Subscriber("/telemetry", Status, ser_callback)
    ser_cmd = ser.Serial('/dev/serial/by-path/pci-0000:00:14.0-usb-0:2.4:1.1',115200)#,timeout=0,parity=ser.PARITY_EVEN,rtscts=1) #USB_VCP serial port timeout=0,parity=ser.PARITY_EVEN,rtscts=1)#CP210 serial port
    telem_pub = rospy.Publisher("feedback",Status,queue_size=1)
    rospy.spin()
