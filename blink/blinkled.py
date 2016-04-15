#!/usr/bin python

import RPi.GPIO as GPIO  # import GPIO library 
import time 

mypin1 = 21
mypin2 = 20

# GPIO pin numbering modes 
# GPIO.BCM (Board numbering, e.g. 21) 
# GPIO.BOARD (physical pins. e.g. 40)


GPIO.setmode(GPIO.BCM) # use BOARD PIN NUMBERING
GPIO.setup(mypin1, GPIO.OUT) # Setup GPIO Pin 7 to OUT
GPIO.setup(mypin2, GPIO.OUT)

def Blink(numTimes, speed): 
	for i in range(0, numTimes): 
		print "Iteration " + str(i+1) # print current loop 
		GPIO.output(mypin1, True)	# switch on pin 7
		GPIO.output(mypin2, True)
		time.sleep(speed)	# wait
		GPIO.output(mypin1, False) 	# switch off pin 7
		GPIO.output(mypin2, False)
		time.sleep(speed) # wait
	print "Done" 
	GPIO.clean() 

Blink(10, 1)

