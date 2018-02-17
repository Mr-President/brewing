import datetime
import os
import time
import Temp
import RPi.GPIO as GPIO
import EmailTest
hstat = True
saverate = 10
maxtd = 60
GPIO.setmode(GPIO.BOARD)
def gettime(lshutoff):
	b = datetime.datetime.now()
	timed = b - lshutoff
	timed = divmod(timed.seconds,60)
	return timed
def setpi(bol,pin):
	a = datetime.datetime.now()
	if bol == True:
		GPIO.output(pin, GPIO.HIGH)
		print "Heat turned on at " + a.strftime("%d/%m/%Y %H:%M:%S")
		stat = "Heater turned on at " + a.strftime("%d/%m/%Y %H:%M:%S")
		global hstat
		hstat = True
		lshutoff = datetime.datetime.now()
		with open(statfil,"w+") as g:
			g.write(stat)
	elif bol == False:
		GPIO.output(pin, GPIO.LOW)
		print "Heater turned off at " + a.strftime("%d/%m/%Y %H:%M:%S")
		stat = "Heater turned off at " + a.strftime("%d/%m/%Y %H:%M:%S")
		global hstat
		hstat = False
		with open(statfil,"w+") as g:
			g.write(stat)


while True:
	try:
		setpoint = int(raw_input("What shoudl the setpoint be? "))
		overt = int(raw_input("What would you like the overshoot to be? "))
		undert = int(raw_input("What would you like the undershoot to be? "))
		pin = int(raw_input("What pin would you like to use? "))
	except ValueError, SyntaxError:
		print "You have entered and invalid character. Only enter numbers."
		continue
	break
GPIO.setup(pin, GPIO.OUT)
dir_path = os.path.dirname(os.path.realpath(__file__))

while True:
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
	
lshutoff = datetime.datetime.now()
try:
	while True:
		print hstat
		td = gettime(lshutoff)
		temdat = Temp.read_temp(setpoint)
		curt = int(float(temdat[1]))
		print curt
		print td
		if td >= saverate:
			temdat = ",".join(temdat)
			with open(datfil,"w+") as f:
				f.write(temdat)
		if hstat == True:
			if curt > setpoint:
				if curt - setpoint > overt:
					setpi(False,pin)
			elif td >= maxtd:
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
		elif hstat == False:
			if setpoint > curt:
				if setpoint - curt > undert:
					setpi(True,pin)
		else:
			pass
		print hstat
		time.sleep(10)
except KeyboardInterrupt:
	print "You have ended control"
	setpi(False, pin)
	GPIO.cleanup()
	a = datetime.datetime.now()
	stat = "Program terminated at " + a.strftime("%d\%m\%Y %H:%M:%S")
	with open (statfil, "w+") as g:
		g.write(stat)
	exit()
except:
	setpi(False,pin)
	GPIO.cleanup()
	EmailTest.error()
	a = datetime.datetime.now()
	stat = "Error occured at " + a.strftime("%d\%m\%Y %H:%M:%S")
	with open(statfil,"w+") as g:
		g.write(stat)
