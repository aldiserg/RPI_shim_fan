#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from subprocess import check_output
from re import findall

dataPIN = 17 # change data pin if needed

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(dataPIN, GPIO.OUT)

tempOn = 50
shim = GPIO.PWM (dataPIN, 10) # pin and speed
shim.start(0)

def get_temp():
    temp = check_output(["vcgencmd","measure_temp"]).decode()    
    temp = float(findall('\d+\.\d+', temp)[0]) # get int from string
    return(temp) 

while True:
	temp = get_temp()
	# print(temp, "C")
	if temp > tempOn+20:
		shim.ChangeDutyCycle(100)
	if temp > tempOn+10:
		shim.ChangeDutyCycle(80)
	if temp > tempOn-10:
		shim.ChangeDutyCycle(50)
	else:
		shim.ChangeDutyCycle(0)
	time.sleep(1)

