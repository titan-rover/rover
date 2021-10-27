#! /usr/bin/env python

import rospy
from std_msgs.msg import Empty
from sensor_msgs.msg import Joy
from basic_arm_controller.msg import serial

#cmd_msg[1] if for j4


def joy_callback(data):
    j1_CW = data.buttons[3]
    j1_CCW = data.buttons[0]

    if j1_CCW == 1 and j1_CW == 0:
        cmds.cmd_msg[3] = '1'
        #print("CCW")

    if j1_CW == 1 and j1_CCW == 0:
        cmds.cmd_msg[3] = '0'
        #print("CW")

    if j1_CCW == 0 and j1_CW == 0:
        cmds.cmd_msg[3] = '2'
        #print("no Movement")

    my_pub.publish(cmds)

rospy.init_node('j1_listener',anonymous=True)
cmds = serial()
my_sub = rospy.Subscriber('joy',Joy,joy_callback)
my_pub = rospy.Publisher('arm_commands',serial,queue_size = 1)
rospy.spin()
