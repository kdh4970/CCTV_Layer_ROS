#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from __future__ import print_function
import rospy				
from CCTV_Layer_ROS.msg import Locations, Coordinate


def points_topic_callback(data):
    loc_size = len(data.location)
    print("-"*10)
    print("Message Sequence:", data.msg_seq)
    print("Locations:")
    for i in range(loc_size):
        print("(", data.location[i].x, ", ", data.location[i].y, ")", end=', ')
    print("\n")
    
def main():
    rospy.init_node('Received_points', anonymous=False)
    rospy.Subscriber("points", Locations, points_topic_callback)

    rospy.spin()

if __name__ == '__main__':
    main()