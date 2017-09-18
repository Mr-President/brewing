import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(14,GPIO.OUT)

p = GPIO.PWM(14,50)
kg = True

speed = str(input('Forward or Back?'))

while True:
	if speed.lower() == 'f':
		p.start(25.0)
	elif speed.lower() == 'b':
		p.start(75.0)
	else:
		print('This is not a correct command')
	kg = input('Keep going?')
	
	if kg.lower() == 'y':
		kg = True
	else:
		break
GPIO.cleanup()
