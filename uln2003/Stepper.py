#! /usr/bin/env python2

import json
import sys
import time
import RPi.GPIO as GPIO

realData=''
realData=realData+sys.argv[1]

data_str = json.loads(realData)
motor_status = 200
motor_status1 = int(data_str['motor'])

print motor_status1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
coil_A_1_pin = 17 # pink
coil_A_2_pin = 18 # orange
coil_B_1_pin = 27 # blue
coil_B_2_pin = 22 # yellow

# adjust if different
#StepCount = 8
#Seq = range(0, StepCount)
#Seq[0] = [0,1,0,0]
#Seq[1] = [0,1,0,1]
#Seq[2] = [0,0,0,1]
#Seq[3] = [1,0,0,1]
#Seq[4] = [1,0,0,0]
#Seq[5] = [1,0,1,0]
#Seq[6] = [0,0,1,0]
#Seq[7] = [0,1,1,0]

StepCount = 4
Seq = range(0, StepCount)
Seq[0] = [1,0,0,0]
Seq[1] = [0,1,0,0]
Seq[2] = [0,0,1,0]
Seq[3] = [0,0,0,1]


#GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

#GPIO.output(enable_pin, 1)

def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)

def forward(delay, steps):
    for i in range(steps):
	for j in range(StepCount):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
	    time.sleep(delay)

def backwards(delay, steps):
    for i in range(steps):
	for j in reversed(range(StepCount)):
	    setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
	    time.sleep(delay)

if __name__ == '__main__':
    delay = 3
    steps = motor_status1
    forward(int(delay) / 1000.0, int(steps))
    GPIO.cleanup()
#    steps = raw_input("How many steps backwards? ")
#    backwards(int(delay) / 1000.0, int(steps))


