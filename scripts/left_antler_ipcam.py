#! /usr/bin/env python
import rospy
import cv2
import os

RTSP_URL = 'rtsp://admin:titanrover2022!@192.168.1.64:554/H265/ch1/main/av_stream'
#RTSP_URL = 'rtsp://admin:123456@192.168.1.67/H264?ch=1&subtype=0'
#RTSP_URL = 'rtsp://admin:123456@192.168.1.36/H264?ch=1&subtype=0'
os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'

cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

if not cap.isOpened():
    print('Cannot open RTSP stream')
    exit(-1)

while True:
    _, frame = cap.read()
    cv2.imshow('RTSP stream', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

















'''
class IP_CAMERA(object):
    def __init__(self,node_name,address):
        self.ip_addr = address
        rospy.init_node(node_name,anonymous=False)
        self._device = cv2.VideoCapture(self.ip_addr)
        self._device.set(cv2.CAP_PROP_BUFFERSIZE,0)
        self._device.set(cv2.CAP_PROP_FRAME_WIDTH,200)
        self._device.set(cv2.CAP_PROP_FRAME_HEIGHT,200)
        rospy.sleep(1)

    def __del__(self):
        self._device.release()

    def get_frame(self):
        ret , frame = self._device.read()
        return frame

    def run(self):
        while not rospy.is_shutdown():
            img = self.get_frame()
            cv2.imshow('frame',img)
            cv2.waitKey(1)

node = IP_CAMERA(
    "camera_node",
    "rtsp://192.168.1.169:8080/0"
    )
node.run()
'''
