#! /usr/bin/env python2
#test code for the process of sending feedback through serial port

import rospy, subprocess, sys
from multijoy.msg import Multi
from mobility.msg import Status
from sensor_msgs.msg import Joy
import serial as ser
ser_cmd = ser.Serial('/dev/serial/by-path/pci-0000:00:14.0-usb-0:2.2:1.0-port0',115200)

def get_feedback(data):
    #ser_cmd.write("hello")# send a command to generate pyboard to send response
    feed_test = ser_cmd.read()#read a line
    feed_test = bytes(feed_test)
    if len(feed_test) > 4:#pyboard has 12 but ADC 0-4095. len cannot be > 4
        pass
    #feed_test = int(feed_test)
    print(feed_test)


if __name__ == '__main__':
    rospy.init_node('pyboard_feedback',anonymous=True)
    rospy.Subscriber("/telemetry", Status, get_feedback)
    rospy.spin()
