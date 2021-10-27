#! /usr/bin/env python2

import rospy
from basic_arm_controller.msg import serial
import serial as ser

def ser_callback(data):
    j5_cmd = data.cmd_msg[0]
    j5_2_cmd = data.cmd_msg[1]
    j4_cmd = data.cmd_msg[2]
    j1_cmd = data.cmd_msg[3]
    if len(j5_cmd) == 0:
        j5_cmd = '3'
    if len(j5_2_cmd) == 0:
        j5_2_cmd = '3'
    if len(j4_cmd) == 0:
        j4_cmd = '3'
    if len(j1_cmd) == 0:
        j1_cmd = '3'

    cmd = [j5_cmd,j5_2_cmd,j4_cmd,j1_cmd]
    cmd = bytearray(cmd)
    #print(cmd)
    ser_cmd.write(cmd)

rospy.init_node('serial_gernerator',anonymous=True)
my_sub = rospy.Subscriber('arm_commands',serial,ser_callback)
ser_cmd = ser.Serial('/dev/serial/by-path/pci-0000:00:14.0-usb-0:1.1.4:1.1',115200) # real serial port
#ser_cmd = ser.Serial('/dev/serial/by-path/pci-0000:00:14.0-usb-0:1.1:1.1',9600)#test serial port
rospy.spin()
