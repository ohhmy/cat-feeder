#! /usr/bin/env python2

import json
import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 

#    StepCount = 4

#GPIO.setup(enable_pin, GPIO.OUT)


def setStep(w1, w2, w3, w4):
    coil_A_1_pin = 17 # pink
    coil_A_2_pin = 18 # orange
    coil_B_1_pin = 27 # blue
    coil_B_2_pin = 22 # yellow
    
    GPIO.setup(coil_A_1_pin, GPIO.OUT)
    GPIO.setup(coil_A_2_pin, GPIO.OUT)
    GPIO.setup(coil_B_1_pin, GPIO.OUT)
    GPIO.setup(coil_B_2_pin, GPIO.OUT)


    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)

def forward(delay, steps):
    Seq = range(0, 4)
    Seq[0] = [1,0,0,0]
    Seq[1] = [0,1,0,0]
    Seq[2] = [0,0,1,0]
    Seq[3] = [0,0,0,1]

    for i in range(steps):
	for j in range(4):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
	    time.sleep(delay)

def backwards(delay, steps):
    for i in range(steps):
	for j in reversed(range(4)):
	    setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
	    time.sleep(delay)

def main(count):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    forward(3/1000.0,count)
    GPIO.cleanup()

if __name__ == '__main__':
    delay = 3
    steps = motor_status
    forward(int(delay) / 1000.0, int(steps))
    GPIO.cleanup()
#    steps = raw_input("How many steps backwards? ")
#    backwards(int(delay) / 1000.0, int(steps))


