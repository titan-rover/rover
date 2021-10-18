#!/usr/bin/env python

'''
File:         roverESC.py
Authors:      Georden Grabuskie / Shripal Rawal / Timothy Parks
Emails:       ggrabuskie@csu.fullerton.edu / rawalshreepal000@gmail.com / parkstimothyj@gmail.com
Description:  sends movement commands to ESC's and updates telemetry data node
'''
import time
import rospy, subprocess, sys
from multijoy.msg import Multi
from mobility.msg import Status
from sensor_msgs.msg import Joy
# To import packages from different Directories
#rootDir = subprocess.check_output('locate TitanRover2019 | head -1', shell=True).strip().decode('utf-8')
#sys.path.insert(0, rootDir + '/build/resources/python-packages')
#from pysaber import DriveEsc
#import pyarm
from roboclaw import Roboclaw
global newtime
global oldtime
oldtime=time.time()
#newtime=time.time()

address = 0x80
rc = Roboclaw("/dev/serial/by-id/usb-03eb_USB_Roboclaw_2x60A-if00",115200)
#rc = Roboclaw("/dev/ttyACM1", 115200)
#f=open("file.txt", "w")
#f.write("TEST")
if not rc.Open():
 print ("***************************FAILED TO OPEN****************************")



rc.ForwardMixed(address, 0)
rc.TurnRightMixed(address, 0)
rc.BackwardMixed(address, 0)
rc.TurnLeftMixed(address, 0)


# Instantiating The Class Object For PySabertooth
#wheels = DriveEsc(128, "mixed")
#armMix = DriveEsc(129, "notMixed")

IDLE_TIMEOUT = 15 #seconds
#use actual button numbers instead of 0-indexed array
j1_b = [0 for i in range(13)]
j1_a = [0.0 for i in range(7)]
j2_b = [0 for i in range(13)]
j2_a = [0.0 for i in range(7)]
j1 = 0.0
j4 = 0
j51 = (0, 0)
j52 = (0, 0)


#comms source for reference (variables not used)
ERROR = -1
LOCAL = 0
GHZ = 1
MHZ = 2
DRIVER = 3

#modes
PAUSE = -1 #LS + B3
IDLE = 0
MOBILITY = 1 #LS + B2
ARM = 2    #LS + B4
BOTH = 3  #R2 + B1
AUTO = 4
#instantiate publisher structure
telem = Status()
telem.source = -1
telem.mode = MOBILITY
telem.throttle = .2
telem.armAttached = False
njoys = 0
#global variables
last_mode = telem.mode
print(telem)
last_active = last_throttle_change = 0
def setStop(): #just set all values on both joysticks to 0
    global j1_a, j1_b, j2_a, j2_b, j1, j4, j51, j52
    j1_a = [0 for i in range(len(j1_a))]
    j1_b = [0 for i in range(len(j1_b))]
    j2_a = [0 for i in range(len(j2_a))]
    j2_b = [0 for i in range(len(j2_b))]
    j1, j4 = 0, 0
    j51 = (0, 0)
    j52 = (0, 0)

def setVals(joy_data):
    global j1_a, j1_b, j2_a, j2_b, j1, j4, j51, j52, njoys
    njoys = joy_data.njoys.data
    for i in range(1, len(j1_a)):
        j1_a[i] = joy_data.joys[0].axes[i-1]
    #for i in range(1, len(j1_b)):
        #j1_b[i] = joy_data.joys[0].buttons[i-1]

    j1 = int(j1_a[5])
    j4 = int(j1_a[6])
    j51 = (j1_b[6], j1_b[8])
    j52 = (j1_b[5], j1_b[7])

    if njoys == 2:
        print("Assigning joy 2")
        for i in range(1, len(j2_a)):
            j2_a[i] = joy_data.joys[1].axes[i-1]
        for i in range(1, len(j2_b)):
            j2_b[i] = joy_data.joys[1].buttons[i-1]
        j1 = ((-1*j2_b[3])+j2_b[4])
        j4 = int(j2_a[5])
        j51 = (j2_b[5], j2_b[6])
        j52 = (j2_b[1], j2_b[2])



def isActive():
    global j1_a, j1_b, j2_a, j2_b
    return not all(v == 0.0 for v in j1_a and j1_b and j2_a and j2_b)

def main(data):
    global oldtime, newtime
    global telem, last_active, last_throttle_change, last_mode, njoys,\
        j1_a, j1_b, j2_a, j2_b, j1, j4, j51, j52
    setVals(data)
    telem.source = data.source

    #wake from idle or set mode to idle
    if isActive():
        last_active = data.header.stamp
        if telem.mode == IDLE:
            telem.mode = last_mode
    elif (rospy.Time.now() - last_active) > rospy.Duration(IDLE_TIMEOUT):
        if (telem.mode != IDLE):
            last_mode = telem.mode
        telem.mode = IDLE
        telem_pub.publish(telem)

    #set mode
    if(telem.source == DRIVER):
        telem.mode = AUTO
        telem_pub.publish(telem)

    if(j1_b[9]):
        if(j1_b[3]):
            telem.mode = PAUSE
        elif(j1_b[2]):
            telem.mode = MOBILITY
        elif(j1_b[4]):
            telem.mode = ARM
            setStop()
        elif(j1_b[1]):
            telem.mode = BOTH
        telem_pub.publish(telem)
    else:
        #single key presses for throttle
        if(j1_b[4] and (telem.throttle < .95) and ((rospy.Time.now() - last_throttle_change) > rospy.Duration(0.25))):
            telem.throttle += 0.1
            last_throttle_change = rospy.Time.now()
        elif (j1_b[2] and (telem.throttle > .25) and ((rospy.Time.now() - last_throttle_change) > rospy.Duration(0.25))):
            telem.throttle -= 0.1
            last_throttle_change = rospy.Time.now()
        #telem_pub.publish(telem)
        try:
           newtime = time.time()
           if True: #newtime - oldtime > 1:
               oldtime = newtime
               print telem.mode
               if True: # telem.mode in {MOBILITY, BOTH}:
                    speed = int(round(j1_a[1] * 80))
                    #print "axis 1, axis 2", j1_a[1], j1_a[2]
                    #print "j1_a[1]: ", j1_a[1]
                    print "speed1", speed
                    if speed > 0:
                        #print "forward: ", abs(speed)
                        rc.ForwardMixed(address, abs(speed))
                    elif speed < 0:
                        #print "backward: ", abs(speed)
                        rc.BackwardMixed(address, abs(speed))
                    else:
                        #print "forward/backward stop "
                        rc.ForwardMixed(address, 0)
                        rc.BackwardMixed(address, 0)
                    #print "j1_a[0]: ", j1_a[0]
                    speed = int(round(j1_a[2] * 80))
                    print "speed2", speed
                    if speed > 0:
                        #print "left: ", abs(speed)
                        rc.TurnRightMixed(address, speed)
                    elif speed < 0:
                        #print "right: ", abs(speed)
                        rc.TurnLeftMixed(address, abs(speed))
                    else:
                        #print "right/left stop "
                        rc.TurnRightMixed(address, 0)
                        rc.TurnLeftMixed(address, 0)
           else:
               print "waiting"
               '''
                #print speed
                if j1_b[1]:
                    print("Turn left")
                    #wheels.driveBoth(0,-63)
                    rc.ForwardMixed(address, 0)
                    rc.BackwardMixed(address, 0)
                    rc.RightMixed(address, 0)
                    rc.LeftMixed(address, 127)
                elif j1_b[3]:
                    print("Turn right")
                    #wheels.driveBoth(0,63)
                    rc.ForwardMixed(address, 0)
                    rc.BackwardMixed(address, 0)
                    rc.LeftMixed(address, 127)
                    rc.RightMixed(address, 127)
                else:
                    #normal movement
                    #if telem.source is 3:
                    #    print("APP DRIVE", j1_a[2], j1_a[1])
                    #    print(j1_a[2], j1_a[1]) 
                    #wheels.driveBoth(int(j1_a[2]),int(j1_a[1]))
                    if j1_a[0] < 0:
                    rc.ForwardBackwardMixed(address, int(j1_a[0]))
                    rc.LeftRightMixed(address, int(j1_a[1]))
                    #else:
                    print("F710 DRIVE", j1_a[0], j1_a[1])
                    print(j1_a[0], j1_a[1]) 
                    #wheels.driveBoth(int(telem.throttle*127*j1_a[2]),int(-1 * telem.throttle*127*j1_a[1]))
                    #rc.ForwardBackwardMixed(address, int(translate(int(telem.throttle*127*j1_a[2]), -127, 127, 0, 127)))
                    #rc.LeftRightMixed(address, int(translate(int(-1*telem.throttle*127*j1_a[1]), -127, 127, 0, 127)))
                    
            elif telem.mode in {AUTO}:
                print("AUTO: ", j1_a[1], j1_a[2])
                #wheels.driveBoth(j1_a[1] , j1_a[2])

            if njoys == 2 and telem.mode in {BOTH, ARM}:
                print("Attack 3d", j2_a[1], j2_a[2], j1, j4, j51, j52)
                #armMix.driveBoth(int(127*j2_a[1]),int(127*j2_a[2]))#j2, j3
                #pyarm.armData(j1, j4, j51, j52) #j1, j4, j51, j52
            elif njoys ==1 and telem.armAttached and telem.mode in {BOTH, ARM}:
                print("F710", j1_a[3], j1_a[4], j1, j4, j51, j52)
                #armMix.driveBoth(int(127*j1_a[3]),int(127*j1_a[4]))#j2, j3
                #pyarm.armData(j1, j4, j51, j52) #j1, j1, j4, j51, j52
                    '''
        except Exception as e:
            print("Mobility-main-drive error")
            print(e)

if __name__ == '__main__':
    try:
        setStop()
        rospy.init_node('rover_mobility', anonymous=True)
        last_active = last_throttle_change = rospy.Time.now()
        telem_pub = rospy.Publisher("telemetry", Status, queue_size=1)
        rospy.Subscriber("/multijoy", Multi, main)

        rospy.spin()
    except(KeyboardInterrupt, SystemExit):
        f.close()
        rospy.signal_shutdown("scheduled")
        raise

