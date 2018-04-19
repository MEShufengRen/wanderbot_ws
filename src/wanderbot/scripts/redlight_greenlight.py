#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

cmd_vel_pub=rospy.Publisher('cmd_vel',Twist,queue_size=1)
rospy.init_node('redlight_green_light')

redlight_twist=Twist()
greenlight_twist=Twist()
greenlight_twist.linear.x=0.5

driving_forward=False
light_change_time=rospy.Time.now()
rate=rospy.Rate(10)

while  not rospy.is_shutdown():
	if driving_forward:
		cmd_vel_pub.publish(greenlight_twist)
	else:
		cmd_vel_pub.publish(redlight_twist)
	if light_change_time<rospy.Time.now():
		driving_forward= not driving_forward
		light_change_time=rospy.Time.now()+rospy.Duration(3)
	rate.sleep()

