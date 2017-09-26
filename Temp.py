import os
import time
import datetime
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temp_sensor = '/sys/bus/w1/devices/28-0417030a23ff/w1_slave'

def temp_raw():
	f = open(temp_sensor, 'r')
	lines = f.readlines()
	f.close()
	return lines
def read_temp():

	lines = temp_raw()
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		lines = temp_raw()
	temp_output = lines[1].find('t=')

	if temp_output != -1:
		temp_string = lines[1].strip()[temp_output+2:]
		temp_f = (float(temp_string)/1000.0)*9.0/5.0+32.0
		return [temp_f,datetime.datetime.now().strftime("%H:%M:%S"),datetime.datetime.now().strftime("%d-%m-%y")]
while True:
	print(read_temp())
	time.sleep(5)
