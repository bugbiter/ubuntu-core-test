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
    GPIO.setup(21, GPIO.IN)	

    # Every second read input
    while True:
        val = GPIO.input(21)
        print("GPIO21 = {}", format(val))
        time.sleep(1)

if __name__ == '__main__':
    main()