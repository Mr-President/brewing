import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12,50)
pwm.start(0)

def setangle(angle):
  duty = 75.0
  GPIO.output(12, True)
  pwm.ChangeDutyCycle(duty)
  sleep(5)
  GPIO.output(12, False)
  pwm.ChangeDutyCycle(0)
  
setangle(90)
pwm.stop()
GPIO.cleanup()
