#! /usr/bin/env python

import rospy
from std_msgs.msg import Empty
from sensor_msgs.msg import Joy
from basic_arm_controller.msg import serial

#cmd_msg[1] if for j4


def joy_callback(data):
    j4_cmd = data.axes[1]

    if j4_cmd > 0.5:
        cmds.cmd_msg[2] = '1'
        #print("CCW")

    elif j4_cmd < -0.5:
        cmds.cmd_msg[2] = '0'
        #print("CW")
    else:
        cmds.cmd_msg[2] = '2'
        #print("no Movement")

    my_pub.publish(cmds)

rospy.init_node('j4_listener',anonymous=True)
cmds = serial()
my_sub = rospy.Subscriber('joy',Joy,joy_callback)
my_pub = rospy.Publisher('arm_commands',serial,queue_size = 1)
rospy.spin()
