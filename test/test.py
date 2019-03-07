#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

# Set up PIN 21 as input
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(0, GPIO.IN)	

#on = True

# Every second read input
while True:
#    GPIO.output(0, on)
#    on = not on
    val = GPIO.input(21)
    print "GPIO21 = {val}"
    time.sleep(1)