#! /usr/bin/env python2

import rospy, subprocess, sys
from mobility.msg import Status



def print_callback(data):
    wheel1 = data.wheel1_amps
    #wheel2 = data.wheel2_amps
    #wheel3 = data.wheel3_amps
    #wheel4 = data.wheel4_amps
    print(wheel1)#wheel2,wheel3,wheel4)





if __name__ == '__main__':
    rospy.init_node('current_display',anonymous=True)
    sub = rospy.Subscriber("/telemetry", Status, print_callback)
    rospy.spin()
