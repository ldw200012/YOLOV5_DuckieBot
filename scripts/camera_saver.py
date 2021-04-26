#!usr/bin/env python
import rospy
from PIL import Image
import numpy as np
from sensor_msgs.msg import CompressedImage


def callback(data):
	pub = rospy.Publisher('camera_input_check', CompressedImage, queue_size=10)
	pub.publish(len(data))

	data = np.array(data)
	data = data.reshape((480, 640))

	rescaled = (255.0 / data.max() * (data - data.min())).astype(np.uint8)

	# w, h = 480, 640
	# data = np.zeros((h, w, 3), dtype=np.uint8)
	# data[0:240, 0:320] = [255, 0, 0] # red patch in upper left
	# img = Image.fromarray(data, 'RGB')
	
	img = Image.fromarray(rescaled)
	img.save('my.png')


def camera_saver():
	rospy.init_node('camera_node', anonymous=True)
	rate = rospy.Rate(50)

	for i in range(1): # 500
		sub = rospy.Subscriber("/JoudiDuck/camera_node/image/compressed", CompressedImage, callback)
		rate.sleep()


if __name__=='__main__':
	try:
		camera_saver()
	except rospy.ROSInterruptException:
		pass