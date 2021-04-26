#!usr/bin/env python
import rospy
from PIL import Image
import numpy as np
from sensor_msgs.msg import Image


def callback(data):
	pub = rospy.Publisher('camera_input_check', Image, queue_size=10)
	pub.publish(data)
	print(len(data))
	# img_array = np.array(data.data)
	# img_array = img_array.reshape((480, 640))

	# rescaled = (255.0 / img_array.max() * (img_array - img_array.min())).astype(np.uint8)

	# # w, h = 480, 640
	# # data = np.zeros((h, w, 3), dtype=np.uint8)
	# # data[0:240, 0:320] = [255, 0, 0] # red patch in upper left
	# # img = Image.fromarray(data, 'RGB')

	# img = Image.fromarray(rescaled)
	# img_name = "duckie_"+str(data.header.seq)
	# img.save(img_name)


def camera_saver():
	rospy.init_node('camera_node', anonymous=True)
	rate = rospy.Rate(50)

	while 1: # 500
		# rosrun image_transport republish compressed in:=/JoudiDuck/camera_node/image raw out:=/JoudiDuck/camera_node/image/raw
		sub = rospy.Subscriber("/JoudiDuck/camera_node/image/raw", Image, callback)
		rate.sleep()


if __name__=='__main__':
	try:
		camera_saver()
	except rospy.ROSInterruptException:
		pass