# converts incoming data array from temperature measurments
# The incoming data should be of the form [Temp, Time, Date] this is put into a dictionary
# The dictionary can then be converted into a comma delimited file at the end of the program

import os
import time
import Temp
dir = "/home/pi/brewing/temps"

def inti(dir):
	file = str(raw_input("What Would you "))
	if ".txt" in file == true:
		file = file
	else:
		file += ".txt"
		fi = dir + file
	f = open("file","w+")
	f.close()
	return fi
def write(dir):
	inti(dir)
	f = open(fi,"w+")
	while true:
		a = read_temp()
		f.write(a)
		time.sleep(60)


