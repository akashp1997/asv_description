cmake_minimum_required(VERSION 2.8.3)
project(asv_description)

find_package(catkin COMPONENTS 
	xacro
	robot_state_publisher
	urdf
)

catkin_package(
  CATKIN_DEPENDS xacro robot_state_publisher urdf
)

install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
  PATTERN ".svn" EXCLUDE)