#!/usr/bin/env/python

import rospy
from topic_tutorial_2.msg import MyMsgs
NAME_TOPIC='/msgs_talk'
NAME_NODE='pub_node'

def callback(msgs):
    rospy.loginfo(-1*msgs.x[2]+3*msgs.y[2])

if __name__=='__main__':
    rospy.init_node(NAME_NODE, anonymous=True)
    sub=rospy.Subscriber(NAME_TOPIC,MyMsgs,callback)
    rospy.spin()