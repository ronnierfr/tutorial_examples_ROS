#!/usr/bin/python

import Fuzzy_angular 
import rospy
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from laser_geometry import LaserProjection
import sensor_msgs.point_cloud2 as pc2
from numpy  import array
import math

#Fuzzy variable
Fangular = ctrl.ControlSystemSimulation(Fuzzy_angular.tipping_ctrl)



vLinear = 0.15;
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

#Grab the LIDAR information and return an array of 3D points
laser_projector = LaserProjection();
def getLidar():
   msg = rospy.wait_for_message("/scan", LaserScan)
   cloud = laser_projector.projectLaser(msg)
   gen = pc2.read_points(cloud, skip_nans=True, field_names=("x","y"))
   xyz_generator = [];
   for p in gen:
      xyz_generator.append([p[0],p[1]])
   return array(xyz_generator);

#Displays the 3D points of the screen
def plot3Dpoints(x,y):
	fig = pyplot.figure()
	ax = Axes3D(fig)
	ax.scatter(x,y)
	pyplot.show()


def euc_distance(p1,p2):
	return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


#ROS init node
rospy.init_node('ROS-Python-Vrep', anonymous=True)


msg = Twist()

smaller = 10;

#Apply Fuzzy
while True:
	xyz = getLidar()
	#plot3Dpoints(xyz[:,0],xyz[:,1]);
	
	y = 0;
	smaller = 10;
	for x in xyz:
	   temp = euc_distance(x, [0,0,0]);
	   if temp < smaller:
		y = x[1]; 
		smaller = temp

	   temp = 0;
	

	Fangular.input['distanciaY'] = y
	Fangular.compute()

	outAng = Fangular.output['vAngular']
	print outAng
	msg.linear.x = vLinear	
	msg.angular.z = outAng
	pub.publish(msg)
