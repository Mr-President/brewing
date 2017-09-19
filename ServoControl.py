import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

try:
  while True:
    GPIO.output(18, 1)
    sleep(5)
    GPIO.output(18, 0)
    sleep(5)
except KeyboardInterrupt:
  GPIO.cleanup()
