import RPI.GPIO as GPIO
import time

GPIO.setmode(gpio.board)
GPIO.setup(8,GPIO.OUT)

p = GPIO.PWM(8,50)

speed = input('Forward or Back?')

if str.lower(speed) == 'f':
	p.start(10.0)
elif str.lower(speed) == 'b':
	p.start(75.0)
else:
	print('That is not a valid input, please use f for forward or b for back')