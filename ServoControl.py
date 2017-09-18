import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)

p = GPIO.PWM(8,50)

p.start(85.0)
