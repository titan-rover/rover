#! /usr/bin/env python

import rospy, subprocess, sys
from mobility.msg import Status
from std_msgs.msg import Float32


current = Status()
def wheel1_callback(data):
    current.wheel1_amps = data.data
    current_pub.publish(current)
'''
def wheel2_callback(data):
    current.wheel2_amps = data.w2_current
    current_pub.publish(current)

def wheel3_callback(data):
    current.wheel3_amps = data.w3_current
    current_pub.publish(current)

def wheel4_callback(data):
    current.wheel4_amps = data.w4_current
    current_pub.publish(current)
    '''

if __name__ == '__main__':
    rospy.init_node('current_tracker',anonymous=True)
    wheel1 = rospy.Subscriber("/wheel1", Float32, wheel1_callback)
    #wheel2 = rospy.Subscriber("/wheel2", Float32, wheel2_callback)
    #wheel3 = rospy.Subscriber("/wheel3", Float32, wheel3_callback)
    #wheel4 = rospy.Subscriber("/wheel4", Float32, wheel4_callback)
    current_pub = rospy.Publisher("feedback",Status,queue_size=1)
    rospy.spin()
