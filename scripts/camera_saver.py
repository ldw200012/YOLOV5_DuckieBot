#!usr/bin/env python
import rospy
from sensor_msgs.msg import CompressedImage

image_count = 0


def callback(data):
	pub = rospy.Publisher('camera_input_check', CompressedImage, queue_size=100)
	pub.publish(data)

	image_count += 1


def camera_saver():
	rospy.init_node('camera_node', anonymous=True)
	rate = rospy.Rate(50)

	while image_count < 10: # 500
		sub = rospy.Subscriber("/JoudiDuck/camera_node/image/compressed", CompressedImage, callback)
		rate.sleep()


if __name__=='__main__':
	try:
		camera_saver()
	except rospy.ROSInterruptException:
		pass