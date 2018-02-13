import datetime
import os
import time
import Temp
import RPi.GPIO as GPIO
updaterate = 5
maxtd = 3600
setpoint = 80 # set the set point of the controller here
lshutoff = datetime.datetime.now() # gets the time the heater was last shut off
overt = 0 # the temperature over the set point at which the heater turns off zero for now
undert = 3 # the temperature at which the heater turns on
timed = 0 # the time difference when the script starts
GPIO.setmode(GPIO.BOARD)
dir_path = os.path.dirname(os.path.realpath(__file__))
stat = False

datfil = raw_input("what would you like to name the data file") # the file for saving data
if ".txt" in datfil == True:
	datfil=  dir_path + datfil
elif ".txt" in datfil == False:
	datfil = dir_path + datfil +".txt"
statfil = raw_input("what woud you like to name the status file") # the file for saving the state and chagnes
if ".txt" in statfil == True:
	datfil= dir_path + datfil
elif ".txt" in statfil == False:
	datfil = dir_path + datfil +".txt"

pin = int(raw_input("What pin are should be used?")) # get output pin for heater control
if type(pin) != int: # check if input is a int
	while type(pin) != int: # if it is not an int dont proceed until it is
		pin = raw_input("Please enter only numbers.")
GPIO.setup(pin,GPIO.OUT) # set up the specified GPIO pin
	
def gettime(lshutoff): # get the differential time time from last shut off
	timed = datetime.datetime.now() - lshutoff #provides time difference
	return timed # returns time difference

def setpi(bol): #turns the controller on or off and prints the state with the time
	if bol == True: #turns
		GPIO.output(pin,GPIO.HIGH)
		print "Heater turned on at " + datetime.datetime.now()
		stat = "Heater turned on at " + datetime.datetime.now() + "\n"
		with open(datfil) as g:
			g.write(stat)
	elif bol == False: #turns the controller on or off and prints the state with the time
		GPIO.output(pin,GPIO.LOW)
		print "Heater turned off at " + datetime.datetime.now()
		stat = "Heat turned off at "+ datetime.datetime.now() + "\n"
		with open(datfil) as g:
			g.write(stat)

with open("datfil","w+") as f:
	f.write("Setpoint, Temp, Time, Date\n")
with open("statfil","w+") as g:
	g.write("Status and Time\n")


while True:
	try: 
		tempdat = Temp.read_temp(setpoint)
		curt = tempdat(1)
		tempdat = ",".join(tempdat) +"\n"
		with open ("datfil","w+") as f:
			f.write(tempdat)
		if stat == True:
			if curt - setpoint >= overt:
				setpi(False)
			elif gettime(lshutoff) >= maxtd:
				lshutoff = datetime.datetime.now()
				setpi(False)
				print "Cycling to prevent auto shutoff"
				with open("statfil","w+") as g:
					stat = "Power cycle to prevent automatic shutoff at " + datetime.datetime.now + "\n"
					g.write(stat)
				time.sleep(5)
				setpi(True)
		if stat == False:
			if setpoint - curt >= undert:
				setpi(True)
		time.sleep(updaterate)
	except KeyboardInterrupt:
		print "You have ended the control"
		setpi(False)
		GPIO.cleanup()
		stat ="Program terminated at " + datetime.datetime.now() + "\n"
		exit()
	except:
		print "Unexpected Error Occured"
		setpi(False)
		GPIO.cleanup()
		stat = "Error occured at " + datetime.datetime.now() + "\n"
		with open("statfil","w+") as g:
			g.write(stat)
		exit()
finally:
	GPIO.cleanup()
