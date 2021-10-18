import time
from roboclaw import Roboclaw
address = 0x80
#Windows comport name
#rc = Roboclaw("COM11",115200)
#Linux comport name
rc = Roboclaw("/dev/serial/by-id/usb-03eb_USB_Roboclaw_2x60A-if00",115200)

rc.ForwardMixed(address, 0)
rc.TurnRightMixed(address, 0)
while 1:
	#Get version string
	#rc.ForwardMixed(address, 0)
	rc.ForwardM1(address, 0)
 	#rc.TurnRightMixed(address, 0)
	time.sleep(0.02)

	'''	
	version = rc.ReadVersion(address)
	if version[0]==False:
		print ("GETVERSION Failed")
	else:
		print (repr(version[1]))
	time.sleep(1)
	'''
