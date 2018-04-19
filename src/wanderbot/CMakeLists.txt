cmake_minimum_required(VERSION 2.8.3)
project(wanderbot)
find_package(catkin REQUIRED COMPONENTS geometry_msgs rospy sensor_msgs message_generation)

##Generate messages in the 'msg' folder
#add_message_files(FILES)
#add_service_files(FILES)

## Generate added messages and services with any dependencies listed here
generate_messages(DEPENDENCIES geometry_msgs sensor_msgs)

## Declare a catkin package
catkin_package(CATKIN_DEPENDS geometry_msgs rospy sensor_msgs message_runtime)

#catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES wanderbot
#  CATKIN_DEPENDS geometry_msgs rospy sensor_msgs
#  DEPENDS system_lib
#)

