import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)

p = GPIO.PWM(8,50)
kg = True

speed = input('Forward or Back?')

while True:
	if lower.(speed) == 'f':
		p.start(15.0)
	elif lower.(speed) == 'b':
		p.start(75.0)
	else:
		pritn('This is not a correct command')
	kg = input('Keep going?')
	
	if lower.(kg) == 'y':
		kg = True
	else:
		kg = False
GPIO.cleanup()
