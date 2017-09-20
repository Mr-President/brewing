import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18,50)

try:
  while True:
    GPIO.output(18, 1)
    pwm.start(0)
    pwm.ChangeDutyCycle(25.0)
    sleep(10)    
except Interrupt:
  GPIO.cleanup()
