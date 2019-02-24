#!/usr/bin/env python

################################################################

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image,CompressedImage,Range,Imu
from geometry_msgs.msg import Twist,Pose
import random

import miro_msgs
from miro_msgs.msg import platform_config,platform_sensors,platform_state,platform_mics,platform_control,core_state,core_control,core_config,bridge_config,bridge_stream

import opencv_apps
from opencv_apps.msg import CircleArrayStamped

import math
import numpy
import time
import sys
from miro_constants import miro

from datetime import datetime

class SadMode():
    def __init__(self):
        ## Node rate
        self.rate = rospy.get_param('rate',200)
        self.pub_platform_control = rospy.Publisher('/miro_sad',platform_control,queue_size=0)

    def miro_sad(self):
        r = rospy.Rate(self.rate)
        q = platform_control()
        while not rospy.is_shutdown():
            q.eyelid_closure = 0.3
            q.body_config = [0.0,1.0,0.2,0.1]
            q.body_config_speed = [0.0,-1.0,-1.0,-1.0]
            q.lights_raw = [0,0,255,0,0,255,0,0,255,0,0,255,0,0,255,0,0,255]
            q.tail = -1.0
            q.ear_rotate = [1.0,1.0]
            q.body_vel.linear.x = 0.0
            q.body_vel.angular.z = 0.2
            self.pub_platform_control.publish(q)
            r.sleep()

if __name__== '__main__':
    rospy.init_node('bad')
    sad = SadMode()
    sad.miro_sad()