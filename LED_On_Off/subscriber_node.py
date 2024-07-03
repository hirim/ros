#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO

LED_PIN = 18  # Define the GPIO pin for the LED

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.LOW)

def callback(data):
    command = data.data
    rospy.loginfo(f"Received: {command}")

    if command == 'on':
        GPIO.output(LED_PIN, GPIO.HIGH)
    elif command == 'off':
        GPIO.output(LED_PIN, GPIO.LOW)

def led_subscriber():
    rospy.init_node('led_subscriber', anonymous=True)
    rospy.Subscriber('led_control', String, callback)
    rospy.spin()

if __name__ == '__main__':
    setup()
    try:
        led_subscriber()
    except rospy.ROSInterruptException:
        GPIO.cleanup()
