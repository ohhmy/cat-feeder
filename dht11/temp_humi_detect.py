#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as GPIO
import dht11

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
t_h_detector = dht11.DHT11(pin = 4)
t_h = t_h_detector.read()

if t_h.is_valid():
    print("Temperature: %d C" % t_h.temperature)
    print("Humidity: %d %%" % t_h.humidity)
else:
    print("Error: %d" % t_h.error_code)
