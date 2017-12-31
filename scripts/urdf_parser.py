#!/usr/bin/env python
import roslib
roslib.load_manifest("urdfdom_py")
import rospy

from urdf_parser_py.urdf import URDF
robot = URDF.from_parameter_server()
print(robot.joints[0])
