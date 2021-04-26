#!usr/bin/env python
import rospy
from PIL import Image
import numpy as np
from sensor_msgs.msg import CompressedImage


def callback(data):
	pub = rospy.Publisher('camera_input_check', CompressedImage, queue_size=100)
	pub.publish(data.shape)

	# w, h = 512, 512
	# data = np.zeros((h, w, 3), dtype=np.uint8)
	# data[0:256, 0:256] = [255, 0, 0] # red patch in upper left
	# img = Image.fromarray(data, 'RGB')
	# img.save('my.png')
	# img.show()


def camera_saver():
	rospy.init_node('camera_node', anonymous=True)
	rate = rospy.Rate(50)

	while 1: # 500
		sub = rospy.Subscriber("/JoudiDuck/camera_node/image/compressed", CompressedImage, callback)
		rate.sleep()


if __name__=='__main__':
	try:
		camera_saver()
	except rospy.ROSInterruptException:
		pass