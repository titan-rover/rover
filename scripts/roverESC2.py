#!/usr/bin/env python

'''
File:         roverESC.py
Authors:      Georden Grabuskie / Shripal Rawal / Timothy Parks
Emails:       ggrabuskie@csu.fullerton.edu / rawalshreepal000@gmail.com / parkstimothyj@gmail.com
Description:  sends movement commands to ESC's and updates telemetry data node
'''
import rospy, subprocess, sys
from multijoy.msg import MultiJoy
from mobility.msg import Status
from sensor_msgs.msg import Joy
# To import packages from different Directories
rootDir = subprocess.check_output('locate TitanRover2019 | head -1', shell=True).strip().decode('utf-8')
sys.path.insert(0, rootDir + '/build/resources/python-packages')
#from pysaber import DriveEsc
#import pyarm
from pysaber_test import DriveEsc
import pyarm2

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
telem.pysaber_port = '128'
telem.pysaber_mode = 'mixed'
telem.pyarm_port = '129'
telem.pyarm_mode = 'notMixed'
telem.source = -1
telem.mode = PAUSE
telem.throttle = .3
telem.armAttached = True
njoys = 0

# Instantiating The Class Object For PySabertooth
wheels = DriveEsc(telem.pysaber_port, telem.pysaber_mode)
armMix = DriveEsc(telem.pyarm_port, telem.pyarm_mode)

#global variables
last_mode = telem.mode
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
    for i in range(1, len(j1_b)):
        j1_b[i] = joy_data.joys[0].buttons[i-1]

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
    active = all(v == 0.0 for v in j1_a)
    active += all(v == 0.0 for v in j1_b)
    active += all(v == 0.0 for v in j2_a)
    active += all(v == 0.0 for v in j2_b)
    return False if active == 4 else True 

def main(data):
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
        telem_pub.publish(telem)
        try:
            if telem.mode in {MOBILITY, BOTH}:
                #turn in place
                if j1_b[1]:
                    telem.wheel_action = 'Turn left'
                    telem.pysaber_motor1, telem.pysaber_motor2 = wheels.driveBoth(0,-63)
                elif j1_b[3]:
                    telem.wheel_action = 'Turn right'
                    telem.pysaber_motor1, telem.pysaber_motor2 = wheels.driveBoth(0,63)
                else:
                    #normal movement
                    telem.wheel_action = 'Driving'
                    if telem.source is 3:
                        print("APP DRIVE", j1_a[2], j1_a[1])
                        telem.pysaber_motor1, telem.pysaber_motor2 = wheels.driveBoth(int(j1_a[2]),int(j1_a[1]))
                    else:
                        print("F710 DRIVE", j1_a[1], j1_a[2])
                        telem.pysaber_motor1, telem.pysaber_motor2 = wheels.driveBoth(int(telem.throttle*127*j1_a[2]),int(-1 * telem.throttle*127*j1_a[1]))
            elif telem.mode in {AUTO}:
                print("AUTO: ", j1_a[1], j1_a[2])
                telem.wheel_action = 'Driving'
                telem.pysaber_motor1, telem.pysaber_motor2 = wheels.driveBoth(j1_a[1] , j1_a[2])

            if njoys == 2 and telem.mode in {BOTH, ARM}:
                print("Attack 3d", j2_a[1], j2_a[2], j1, j4, j51, j52)
                telem.pyarm_motor1, telem.pyarm_motor2 = armMix.driveBoth(int(127*j2_a[1]),int(127*j2_a[2]))#j2, j3
                pyarm2.armData(j1, j4, j51, j52) #j1, j4, j51, j52
            elif njoys ==1 and telem.armAttached and telem.mode in {BOTH, ARM}:
                print("F710", j1_a[3], j1_a[4], j1, j4, j51, j52)
                telem.pyarm_motor1, telem.pyarm_motor2 = armMix.driveBoth(int(127*j1_a[3]),int(127*j1_a[4]))#j2, j3
                pyarm2.armData(j1, j4, j51, j52) #j1, j1, j4, j51, j52
        except Exception as e:
            print("Mobility-main-drive error")
            print(e)

if __name__ == '__main__':
    try:
        setStop()
        rospy.init_node('rover_mobility', anonymous=True)
        last_active = last_throttle_change = rospy.Time.now()
        telem_pub = rospy.Publisher("telemetry", Status, queue_size=1)
        rospy.Subscriber("/multijoy", MultiJoy, main)
        rospy.spin() 

    except(KeyboardInterrupt, SystemExit):
        rospy.signal_shutdown("scheduled")
        raise

