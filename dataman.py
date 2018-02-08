# converts incoming data array from temperature measurments
# The incoming data should be of the form [Temp, Time, Date] this is put into a dictionary
# The dictionary can then be converted into a comma delimited file at the end of the program

import os
import time
import Temp
dire = "/home/pi/brewing/temps/"

def inti(dire):
	file = str(raw_input("What Would you like to name this file?"))
	if ".txt" in file == true:
		file = file
	else:
		file += ".txt"
	fi = dire + file
	f = open("fi","w+")
	f.write("Temp, Time, Date\n")
	f.close()
	return fi
def write(dier):
	fi = inti(dire)
	f = open(fi,"w+")
	while True:
		a = ",".join(Temp.read_temp())+"\n"
		f.write(a)
		time.sleep(60)
