#! /usr/bin/env python

import rospy
from std_msgs.msg import Empty
from sensor_msgs.msg import Joy
from basic_arm_controller.msg import serial

#cmd_msg[0] if for gripper

def joy_callback(data):
    wrist_cmd = data.axes[6]
    #print(wrist_cmd)

    if wrist_cmd == 1.0:
        cmds.cmd_msg[0] = '1'
        #print("CW")

    if wrist_cmd == -1.0:
        cmds.cmd_msg[0] = '0'
        #print("CCW")

    if wrist_cmd == -0.0:
        cmds.cmd_msg[0] = '2'
        #print("no Movement")

    my_pub.publish(cmds)

rospy.init_node('wrist_listener',anonymous=True)
cmds = serial()
my_sub = rospy.Subscriber('joy',Joy,joy_callback)
my_pub = rospy.Publisher('arm_commands',serial,queue_size=1)
rospy.spin()
