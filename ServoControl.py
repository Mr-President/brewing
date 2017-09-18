import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)

p = GPIO.PWM(8,50)
kg = True

speed = input('Forward or Back?')

while True:
	if speed.lower() == 'f':
		p.start(15.0)
	elif speed.lower() == 'b':
		p.start(75.0)
	else:
		print('This is not a correct command')
	kg = input('Keep going?')
	
	if kg.lower() == 'y':
		kg = True
	else:
		kg = False
GPIO.cleanup()
