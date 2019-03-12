#!/usr/bin/env python3
# coding=utf-8

import RPi.GPIO as GPIO
import time

__version__ = '0.0.1'

def main():
    print("Starting python-rpi-test")

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
        print("GPIO21 = %i", val)
        time.sleep(1)

if __name__ == '__main__':
    main()