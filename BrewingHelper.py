import os
import time
import dataman
import PID
import Temp
initcond = Temp.read_temp()
setpoint = initcond[1] # gets setpoint from initial condition data
valvset = 0

def startserver(): #place holder for when this starts a web server to display data / graphs

def stopserver(): #place holder to stop server

def gett(): #gets the current temperature from the temp file type
	tdat = Temp.read_temp() #reads data from Temp script which contains date and time the temperature was taken in a vector
	tcur = tdat[1] # strips out just the temperature in F
	return tcur # returns just the tempearture
def start_PID(setpoint,): #start the PID controller this should initalize with the default gains
	controller = PID() #initialize controller as a PID object
	controller.setPoint(setpoint)
	curt = gett() #get current temperature
	vset = controller.update(curt) #pulls up the initial valve setting from controller update
	return vset
def open_n_light(): #opens the burn and lights at 100%
	valvset = 100 #open valv all the way or to 100 of allowable range
	while islit() == False: # check if flame is lit and continue while it is not
		light(True)
		setvalv(valvset)
		


	valvset = getvalnew()# get the setting that should be
	setvalv(valvset)


def getvalvnew(cont): #update valve position after initialize
	curt = gett() # get temperature
	vset = cont.update(curt) #get the valve setting from the PID controller
	return vset #return the valve setting
def setvalv(vset):
	if vset == valvset: #check if valve is already at desire setting, if it is end
		return
	elif:

	valvset = vset # saves the valve setting to global variable so it can be recalled later
def light():#sparks the lighters

def erelight(): # emergency relighting of the burner if it burns out

def eshutdown(): # emergency shut down of the burner if it fails to light
