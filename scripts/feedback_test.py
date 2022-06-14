#! /usr/bin/env python2

import rospy
import serial as ser
from mobility.msg import Status

# Faster way to readline compared to ser.readline()
# https://github.com/pyserial/pyserial/issues/216#issuecomment-369414522
class ReadLine:
    def __init__(self, s):
        self.buf = bytearray()
        self.s = s

    def readline(self):
        i = self.buf.find(b"\n")
        if i >= 0:
            r = self.buf[:i+1]
            self.buf = self.buf[i+1:]
            return r
        while True:
            i = max(1, min(2048, self.s.in_waiting))
            data = self.s.read(i)
            i = data.find(b"\n")
            if i >= 0:
                r = self.buf + data[:i+1]
                self.buf[0:] = data[i+1:]
                return r
            else:
                self.buf.extend(data)

#ser = serial.Serial('COM7', 9600)
#rl = ReadLine(ser)
#
#while True:
#
#    print(rl.readline())
#

def talker():
    msg = Status()
    pub = rospy.Publisher('joint_test', Status, queue_size=1)
    rospy.init_node('custom_talker', anonymous=True)
    r = rospy.Rate(1000)

    '''
    msg.source = 1
    msg.armAttached = True
    msg.mode = 0
    msg.throttle = 0
    msg.arm_action = '0'
    msg.wheel_action = '0'
    msg.wheel_action = '0'
    msg.pysaber_mode = '0'
    msg.pysaber_cmd = '0'
    msg.pysaber_motor1 = '0'
    msg.pysaber_motor2 = '0'
    msg.pysaber_send = '0'
    msg.pysaber_port = '0'
    msg.pyarm_motor1 = '0'
    msg.pyarm_motor2 = '0'
    msg.pyarm_port = '0'
    msg.pyarm_mode = '0'
    strippedFeed = "0"
    '''




    while not rospy.is_shutdown():

        feed = str(rl.readline())
        msg.j1_fb = feed
        #feed  = ser_cmd.readline()
        #msg.j1_fb = feed.strip("\0")
        rospy.loginfo(msg.j1_fb)
        strippedFeed = feed.strip("\r\n")
        try:
            msg.j1_fb, msg.j2_fb, msg.j3_fb, msg.j4_fb, msg.j5_wrist_fb = strippedFeed.split(':')
            msg.j1_fb = msg.j1_fb.rstrip()
            msg.j2_fb = msg.j2_fb.lstrip().rstrip()
            msg.j3_fb = msg.j3_fb.lstrip().rstrip()
            msg.j4_fb = msg.j4_fb.lstrip().rstrip()
            msg.j5_wrist_fb = msg.j5_wrist_fb.lstrip().rstrip()

        except:
            rospy.loginfo("ERROR: Cannot Split String")
            msg.j1_fb = "-1"
            msg.j2_fb = "-1"
            msg.j3_fb = "-1"
            msg.j4_fb = "-1"
            msg.j5_wrist_fb = "-1"
        pub.publish(msg)
        r.sleep()

if __name__ == '__main__':
    try:
        telem = Status()
        ser_cmd = ser.Serial('/dev/serial/by-path/pci-0000:00:0c.0-usb-0:2:1.1',115200,timeout=0,parity=ser.PARITY_EVEN,rtscts=1)
        rl = ReadLine(ser_cmd)
        talker()
    except rospy.ROSInterruptException:
        pass
