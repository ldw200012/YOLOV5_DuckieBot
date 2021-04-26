#!usr/bin/env python

import rospy
import cv2
import os
# from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage


def callback(data):
	directory = r'..\img'
	os.chdir(directory)


def img_saver():
	rospy.init_node('duckie_img_saver', anonymous=True)
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		frame_image = rospy.Subscriber("/JoudiDuck/camera_node/image/compressed", CompressedImage, callback)

if __name__=='__main__':
	try:
		img_saver()
	except rospy.ROSInterruptException:
		pass