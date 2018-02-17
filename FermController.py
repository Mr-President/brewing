import datetime #importing shit
import os
import time
import Temp
import RPi.GPIO as GPIO
import EmailTest
import pdb
hstat = False #set the initial status of the heater as off because it is
saverate = 10 # how often I want to save the temperature data in minutes
maxtd = 60 # how often the heater need to cycle to prevent it from shutting off since I am using an electric blanket that wasnt made for this
GPIO.setmode(GPIO.BOARD) #set the pin number for the pi GPIO board to BOARD instead of BCM because BCM is fucking stupid
def gettime(lshutoff): # this function gets the difference in time between the last shutoff and now
	b = datetime.datetime.now() # the time now
	timed = b - lshutoff # a datetime delta between now and last shut off
	timed = divmod(timed.seconds,60) #convert it to minutes
	return timed[0]# get the part thats not the remainder
def setpi(bol,pin): # this function sets the output of the pines
	a = datetime.datetime.now() # gets the time now for saving the temperature data to datfil
	if bol: # checks if the bol argument is True
		GPIO.output(pin, GPIO.HIGH) # if it is True it sets the out put on teh pin to HIGH
		print "Heat turned on at " + a.strftime("%d/%m/%Y %H:%M:%S") # it prints that it turned the heater on
		stat = "Heater turned on at " + a.strftime("%d/%m/%Y %H:%M:%S") #it creates a status that the heater is on
		global hstat #I dont really know it imports a global var or something
		hstat = True # it ideally should update the global var
		lshutoff = datetime.datetime.now() # it sets the last shut off to right now since it just turned on
		with open(statfil,"w+") as g: # it writes the temeprature data
			g.write(stat)
	elif bol == False: # but zach what if its not true well then it goes here
		GPIO.output(pin, GPIO.LOW) # it sets the output to low
		print "Heater turned off at " + a.strftime("%d/%m/%Y %H:%M:%S") #does the same thing that the previous thing did as far as status
		stat = "Heater turned off at " + a.strftime("%d/%m/%Y %H:%M:%S")
		global hstat# the same possiable import thing
		hstat = False#chagne var
		with open(statfil,"w+") as g:#writes stat
			g.write(stat)


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
GPIO.setup(pin, GPIO.OUT) # sets the pin number to an output in
dir_path = os.path.dirname(os.path.realpath(__file__)) # finds current directory

while True: #this works
	try:
		datfil = str(raw_input("What would you like to name the data file? "))
		if datfil.endswith('.txt'):
			datfil = dir_path + "/" + datfil
		elif not datfil.endswith('.txt'):
			datfil = dir_path + "/" + datfil + ".txt"
		statfil = raw_input("What would you like to name the status file? ")
		if statfil.endswith('.txt'):
			statfil = dir_path + "/" + statfil
		elif not statfil.endswith('.txt'):
			statfil = dir_path +"/"+statfil + ".txt"
	except:
		print "You have enetered an invalid character in a file name please try again."
		continue
	break
	
lshutoff = datetime.datetime.now() #creates the first lshutoff value
try:
	pdb.set_trace()
	while True:
		td = gettime(lshutoff) #gets time difference from gettime
		temdat = Temp.read_temp(setpoint) #gets tempdata from read_temp
		curt = int(float(temdat[1])) #gets the current temperature from tempdata because its all a messy ass string
		if td >= saverate: # checks if the time difference is greater than the save rate
			temdat = ",".join(temdat) # if it is it creates a single coma delimited string 
			with open(datfil,"w+") as f:#saves the string to the data file
				f.write(temdat)
		if hstat: # if the heater is on its going to check if the temperature is above the ssetpoint
			if curt > setpoint:
				if curt - setpoint > overt: # if it is above the setpoitn by more than the over t
					setpi(False,pin) # it turns off the heater using setpi
			elif td >= maxtd: # if the heater has been on for longer than the max td it power cycles becuase otherwise the heater shuts off
				setpi(False,pin)
				print "Cycling to prevennt auto shuttoff"
				a = datetime.datetime.now()
				stat = "Power cycled at " + a.strftime("%d/%m/%Y %H:%M:%S")
				with open(statfil,"w+") as g:
					g.write(stat)
				time.sleep(5)
				setpi(True,pin)
			else:
				pass
		elif not hstat: # it checks if the heater is off
			if setpoint > curt: # if the temperature is lower than the set point
				if setpoint - curt > undert: # if it is lower by more than the undert
					setpi(True,pin) #if it is turn the heater off
		time.sleep(10) #sleep because I dont need constant update
except KeyboardInterrupt: #what to do if I hit ctrl c
	print "You have ended control"
	setpi(False, pin)
	GPIO.cleanup()
	a = datetime.datetime.now()
	stat = "Program terminated at " + a.strftime("%d\%m\%Y %H:%M:%S")
	with open (statfil, "w+") as g:
		g.write(stat)
	exit()
except: #everhting else
	setpi(False,pin)
	GPIO.cleanup()
	EmailTest.error()
	a = datetime.datetime.now()
	stat = "Error occured at " + a.strftime("%d\%m\%Y %H:%M:%S")
	with open(statfil,"w+") as g:
		g.write(stat)
