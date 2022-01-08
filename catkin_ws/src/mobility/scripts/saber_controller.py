#! /usr/bin/env python

import rospy
from pySaber import DriveEsc
from std_msgs.msg import Empty
from sensor_msgs.msg import Joy

ESC_ADDRESS = 128
ESC_MODE = "notMixed"

def joy_callback(data):
    #for j2 commands
    j2_button_fwd = data.buttons[1]
    j2_button_bck = data.buttons[2]
    #for j3 commands
    j3_button_fwd = data.buttons[5]
    j3_button_bck = data.buttons[4]

    if(j2_button_fwd == 1 or j2_button_bck == 1 or j3_button_fwd == 1 or j3_button_bck == 1):
        if(j3_button_fwd == 1):
            linear_actuators.send(4,127)
        if(j3_button_bck == 1):
            linear_actuators.send(5,127) #if not stop LA
        if(j2_button_fwd == 1):
            linear_actuators.send(1,127)
        if(j2_button_bck == 1):
            linear_actuators.send(0,127) #if not stop LA
        linear_actuators.send(1,0)
        linear_actuators.send(4,0)


rospy.init_node('Saber',anonymous=True)
my_sub = rospy.Subscriber('joy',Joy,joy_callback)
linear_actuators = DriveEsc(ESC_ADDRESS,ESC_MODE)

rospy.spin()
