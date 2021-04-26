#!usr/bin/env python

from sensor_msgs.msg import CompressedImage


def callback(data):
	pub = rospy.Publisher('camera_input_check', CompressedImage, queue_size=100)
	pub.publish(data)


def camera_saver():
	import rospy
	
	rospy.init_node('camera_node', anonymous=True)
	rate = rospy.Rate(50)

	while not rospy.is_shutdowm():
		sub = rospy.Subscriber("/JoudiDuck/camera_node/image/compressed", CompressedImage, callback)
		rate.sleep()


if __name__=='__main__':
	try:
		camera_saver()
	except rospy.ROSInterruptException:
		pass