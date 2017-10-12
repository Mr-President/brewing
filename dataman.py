# converts incoming data array from temperature measurments
# The incoming data should be of the form [Temp, Time, Date] this is put into a dictionary
# The dictionary can then be converted into a comma delimited file at the end of the program

import os
import time
import Temp
dir = "/home/pi/brewing/temps"

def inti(dir):
	file = str(raw_input("What Would you like to name this file?"))
	if ".txt" in file == true:
		file = file
	else:
		file += ".txt"
		fi = dir + file
	f = open("fi","w+")
	f.write("Temp, Time, Date")
	f.close()
	return fi
def write(dir):
	fi = inti(dir)
	f = open(fi,"w+")
	while True:
		a = ",".join(Temp.read_temp())+"\n"
		f.write(a)
		time.sleep(60)
while True:
	write(dir)
