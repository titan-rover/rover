#! /usr/bin/env python

import rospy, subprocess, sys
from multijoy.msg import Multi
from mobility.msg import Status
from pySaber import DriveEsc

ESC_ADDRESS = 128
ESC_MODE = "notMixed"

IDLE_TIMEOUT = 15 #seconds
#use actual button numbers instead of 0-indexed array
j1_b = [0 for i in range(11)]
j1_a = [0.0 for i in range(9)]
j2_b = [0 for i in range(11)]
j2_a = [0.0 for i in range(9)]
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
TYPER = 3
BOTH = 4  #R2 + B1
AUTO = 5

#instantiate publisher structure
telem = Status()
telem.source = -1
telem.mode = PAUSE
njoys = 0

last_mode = telem.mode
last_active = 0
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


def saber_callback(data):

    global telem, last_active, last_mode, njoys,\
        j1_a, j1_b, j2_a, j2_b, j1, j4, j51, j52
    setVals(data)
    telem.source = data.source
    if isActive():
        last_active = data.header.stamp
        if telem.mode == IDLE:
            telem.mode = last_mode
    elif (rospy.Time.now() - last_active) > rospy.Duration(IDLE_TIMEOUT):
        if (telem.mode != IDLE):
            last_mode = telem.mode
        telem.mode = IDLE
        telem_pub.publish(telem)

    if(j1_b[9]):
        if(j1_b[3]):
            telem.mode = PAUSE
        elif(j1_b[2]):
            telem.mode = MOBILITY
        elif(j1_b[4]):
            telem.mode = ARM
            setStop()
        elif(j1_b[10]):
            telem.mode = TYPER
        elif(j1_b[1]):
            telem.mode = BOTH
        print(telem.mode)
        telem_pub.publish(telem)

    if(telem.mode in {ARM,BOTH}):
    #for j2 commands
       j2_button_fwd = j1_b[2]
       j2_button_bck = j1_b[3]
    #for j3 commands
       j3_button_fwd = j1_b[6]
       j3_button_bck = j1_b[5]
       if(j3_button_fwd):
           print("j3fwd")
           linear_actuators.send(4,127)
           #linear_actuators.send(0,0)
       elif(j3_button_bck):
           linear_actuators.send(5,127) #if not stop LA
          # linear_actuators.send(1,0)
           print("j3bck")
       else:
           linear_actuators.send(4,0)
           linear_actuators.send(5,0)
       if(j2_button_fwd):
           linear_actuators.send(1,127)
          # linear_actuators.send(5,0)
           print("j2fwd")

       elif(j2_button_bck):
           linear_actuators.send(0,127) #if not stop LA
           #linear_actuators.send(4,0)
           print("j2bck")
           #linear_actuators.send(1,0)
           #linear_actuators.send(4,0)
       else:
           linear_actuators.send(0,0)
           linear_actuators.send(1,0)


if __name__ == '__main__':
    try:
        setStop()
        rospy.init_node('Saber',anonymous=True)
        last_active = rospy.Time.now()
        linear_actuators = DriveEsc(ESC_ADDRESS,ESC_MODE,'/dev/serial/by-path/pci-0000:00:14.0-usb-0:2.3:1.0-port0')
        rospy.Subscriber("/multijoy", Multi, saber_callback)
        telem_pub = rospy.Publisher("telemetry", Status, queue_size=1)
        rospy.spin()

    except(KeyboardInterrupt, SystemExit):
        rospy.signal_shutdown("scheduled")
        raise
