import time
from Temp import read_fint
import EmailTest
import pdb
import RPi.GPIO as GPIO
from Heater import Heater
tdm = 60

while True: #all this shit gets user inputs for setpoints undert overt and output pin
	try:
		setpoint = int(raw_input("What shoudl the setpoint be? "))# setpoint is setpoint
		overt = int(raw_input("What would you like the overshoot to be? "))# overt is the overshoot value so how far it goes over before shutting off
		undert = int(raw_input("What would you like the undershoot to be? "))# undert is the opposite of over t
		pin = int(raw_input("What pin would you like to use? ")) # pin is which pin is it
	except ValueError, SyntaxError:
		print "You have entered and invalid character. Only enter numbers."
		continue
	break
t = read_fint()
heater = Heater(pin,t,setpoint,undert,overt)
try:
	while True:
		pdb.set_trace()
		t = read_fint()
		heater.update(t)
		time.sleep(5)
except KeyboardInterrupt: #what to do if I hit ctrl c
	print "You have ended control"
	heater.heateroff()
	GPIO.cleanup()
#except: #everhting else
	#heater.heateroff()
	#GPIO.cleanup()
	#EmailTest.error()
