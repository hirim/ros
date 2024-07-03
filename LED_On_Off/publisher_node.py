#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def led_publisher():
    rospy.init_node('led_publisher', anonymous=True)
    pub = rospy.Publisher('led_control', String, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        command = input("Enter 'on' to turn LED on or 'off' to turn LED off: ")
        if command in ['on', 'off']:
            rospy.loginfo(f"Publishing: {command}")
            pub.publish(command)
        else:
            rospy.logwarn("Invalid command. Please enter 'on' or 'off'.")
        rate.sleep()

if __name__ == '__main__':
    try:
        led_publisher()
    except rospy.ROSInterruptException:
        pass
