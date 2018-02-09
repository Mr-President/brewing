import os
import time
import datetime
import PID
import Temp
import csv

direc = os.path.dirname(os.path.realpath(__file__)) #"/home/pi/brewing/temps/"
initcond = Temp.read_temp()
setpoint = initcond[1] # gets setpoint from initial condition data
valvset = 0 #initial valv setting will be 0 but will be updated by functioons
vmin = 0 #vmin will be used to set the minimum setting for the valve. Determined by flame outs
vmax = 100 # the maximum a value can ever be is 100% open
temps = [] # temp data will start empty. Will store 2 minutes of data for plotting
runtime = 4200 # one hour and ten minutes of run time
timestart = datetime.datetime.now().time() # time at the start of the program

#TEST LOOP BELOW

with open("Testdata.csv","r") as f # read in the test data from the CSV file
	reader = csv.reader(f)
	data = list(reader)

tinit = gett(temps)
start_PID(setpoint,tinit) # start the PID before enterying the loop
start_dataman(direc) #start the data manager, I am not sure if I will need to create the fi variable but it may need to be fi = start_dataman(direc)
open_n_light() #start the lighting process
loop = 0

try:

	while datetime.datetime.now().time() - timestart < 300: # runs for 5 minutes
		t = gett(temps,loop) # again not sure if I need temps = gett(temps)
		print t
		write_dataman(fi,loop) # add test data to dataman so it just pulls in temperature data
		valvset = getvalvnew(t,controller)
		setvalv(valvset)
		flameout(t,loop)
		time.sleep(1)
		loop += 1
#testing error handaling keyboard interupts so on if works add into final 
	except (KeyboardInterrupt, SystemExit):
		valvset = 0
		setvalv(valvset)
		print "Program stopped by keyboardinterrupt or the program has been closed"



#TEST LOOP ABOVE

def gett(temps,loop): #gets the rolling average of the last five seconds of temperature data
	#tdat = Temp.read_temp() #reads data from Temp script which contains date and time the temperature was taken in a vector
	tdat = ttestdata(loop)
	temps.append(tdat[1]) # appends data to the 120s record
	avg = mean(temps[115:119]) #averages the temperature over the last five seconds or less
	if len(temps) >= 120: #removes any data older than 120s
		del temps[0]
	elif:
		break
def start_PID(setpoint,t): #start the PID controller this should initalize with the default gains
	controller = PID() #initialize controller as a PID object
	controller.setPoint(setpoint)
	valvset = controller.update(t) #pulls up the initial valve setting from controller update
	return valvset
def start_dataman(direc):
	file = str(raw_input("What would you like to name this file?")) # get user input for file name
	if ".txt" in file == True: # check if .txt is already specified
		file = file
	else:
		file += ".txt" #if not add .txt. All files must be saved as .txt
	fi = direc = file #add directory to save the text file
	with open("fi","w=") as f #open the file as f and close the file no matter what
		f.write("Setpoint, Temp, Time, Date\n")  #write the headers
	return fi # return the file name for future writing
def write_dataman(fi): # writing temperature to the file
	with open(fi,"w+") as f
		#f = open(fi,"w+") #open file for read write
		a = ",".join(Temp.read_temp())+"\n" # get the tempeature and date time data
		f.write(a) # write temperature date time data to the file

def open_n_light(): #opens the burn and lights at 100%
	valvset = 100 #open valv all the way or to 100 of allowable range
	while checkflame(): # check if flame is lit and continue while it is not
		light(True)
		setvalv(valvset)
		time.sleep(1)	
	valvset = getvalnew()# get the setting that should be
	setvalv(valvset)

def getvalvnew(t,cont): #update valve position after initialize
	curt = t # get temperature
	vset = cont.update(curt) #get the valve setting from the PID controller
	return vset #return the valve setting
def setvalv(vset):
	if vset == valvset: #check if valve is already at desire setting, if it is end
		print "valve stayed the same"
	elif:
		a = "Valv set to "+ str(vset) # PART OF TEST CODE
		print a

	valvset = vset # saves the valve setting to global variable so it can be recalled later
def light(bol):#sparks the lighters
	if bol == True:
		print "lighting" #PART OF TEST CODE
	if bol == False:
		print "not lighting" #PART OF TEST CODE
		

def checkflame(loop):# function to check the state of the flame FOR TEST PURPOSE
	return flametestdata(loop)
def flamout(t): # flameout relight to flame out shutdown if cant be relit 
	loop = 0
	if checkflame(loop) == True:
		vmin = valvset + 2 # sets the minimum valv setting to the current plus 2
		print vmin
		while checkflame(loop): # checks if flame is out
			if loop => 5:
				valvset = 0
				setvalv(valvset)
				print "Flame has failed to reignite, shutdown initiated. Python will cloes the program must be reinitiated"
				time.sleep(5)
				light(False)#ignitor left until shutdown
				quit() # this if shuts the valve, stops igniting and exits python if the flame fails to ignite after 6s
			else:
				valvset = 100 #sets the valve setting to 100% for lighting
				setvalv(valvset) # sets valve
				light(True) #starts lighter
				time.sleep(1) #sleeps for one second
				loop =+ 1 # iterates loop up
		curt = t() #gets current average temperature
		valvset = cont.update(curt) #gets valves setting based on current temperature
		setvalv(valvset) #sets valve to current desired setting
		break # exits loop
	else:
		break


def mean(nums):
	return float(sum(nums))/max(len(numbs),1)

# testing functions


def ttestdata(loop,data):
	a = loop +1 #account for header
	return data[]
def flametestdata(loop,data):
	a = loop +1 # account for header
	return data[]