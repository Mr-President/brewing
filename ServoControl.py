import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(03, GPIO.OUT)
pwm = GPIO.PWM(03,50)
pwm.start(0)

def setangle(angle):
  duty = angle / 18+2
  GPIO.output(03, True)
  pwm.ChangeDutyCycle(duty)
  sleep(1)
  GPIO.output(03, Flase)
  pwm.ChangeDutyCycle(0)
  
setangle(90)
pwm.stop()
GPIO.cleanup()
