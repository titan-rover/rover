#! /usr/bin/env python

import rospy
from std_msgs.msg import Empty
from sensor_msgs.msg import Joy
from basic_arm_controller.msg import serial


def joy_callback(data):
    j5_2_cmd = data.axes[7]
    #print(j5_2_cmd)

    if j5_2_cmd == 1.0:
        cmds.cmd_msg[1] = '1'
        #print("CW")

    if j5_2_cmd == -1.0:
        cmds.cmd_msg[1] = '0'
        #print("CCW")

    if j5_2_cmd == -0.0:
        cmds.cmd_msg[1] = '2'
        #print("no Movement")

    my_pub.publish(cmds)

rospy.init_node('wrist_ext_listener',anonymous=True)
cmds = serial()
my_sub = rospy.Subscriber('joy',Joy,joy_callback)
my_pub = rospy.Publisher('arm_commands',serial,queue_size=1)
rospy.spin()
