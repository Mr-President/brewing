import os
import time
import datetime
os.system('modprobe w1-gpio') # load the drivers for the GPIO board
os.system('modprobe w1-therm') # load the drivers for the temeprature sensor

temp_sensor = '/sys/bus/w1/devices/28-0417030a23ff/w1_slave' # define serial number and location of temperature file

def temp_raw(): #function to pull in raw temperature
	f = open(temp_sensor, 'r') #assigns the raw temperature information to the value f
	lines = f.readlines() #reads the two lines into "lines"
	f.close() #closes data file
	return lines # returns the raw data as a line

def read_temp(setpoint):
	lines = temp_raw()
	while lines[0].strip()[-3:] != 'YES': #waits for the device to read that it is connected stripping three from the end of the first line
		time.sleep(0.2)
		lines = temp_raw()
	temp_output = lines[1].find('t=') #finds where it says t= and pulls

	if temp_output != -1: #if it does not find t then it will return -1 and the script will wait here
		temp_string = lines[1].strip()[temp_output+2:] #pulls the temperature using the index from read temp
		temp_f = str((float(temp_string)/1000.0)*9.0/5.0+32.0)
		a = datetime.datetime.now()
		c= datetime.datetime.now()
		b = a + datetime.timedelta(0,-18000)
		d = c + datetime.timedelta(0,-18000)
		return [str(setpoint),temp_f,b.strftime("%H:%M:%S"),d.strftime("%d-%m-%y")] #puts temp with time stampmp
