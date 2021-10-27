#! /usr/bin/env python2
import rospy
from basic_arm_controller.msg import feedback_angles
from sensor_msgs.msg import Joy
import serial as ser

def ser_callback(data):
    j2_feed = feedback_ser.read(1)
    print(j2_feed)
    #my_pub.publish(j2_feed)

rospy.init_node('pyboard_feedback',anonymous=True)
my_sub = rospy.Subscriber('joy',Joy,ser_callback)
my_pub = rospy.Publisher('arm_feedback',feedback_angles,queue_size = 1)
feedback_ser = ser.Serial('/dev/ttyACM0',115200) # real serial port
print("HELLO")
rospy.spin()
