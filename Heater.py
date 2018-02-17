#heater class will contain the object heater where the status and the processs of setting the heater output will be contained
import RPi.GPIO as GPIO
import time
import datetime


class Heater:

	def __int__(self, hstat = False, temp = 0,setp = 0,overt=0 ,undert=3, pin,tdmax = 60,):
		self.pin = pin
		self.status = hstat
		self.temperature = temp
		self.setpoint = setp
		self.undershoot = undert
		self.overshoot = overt
		self.deltatmax = tdmax
		self.lastshutoff = datetime.datetime.now()
		self.delta = 0
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.pin, GPIO.OUT)

	def update(self,curt):
		getdeltat()
		if hstat:
			if curt > self.setpoint:
				if curt - self.setpoint > self.overshoot:
					heateron()
			elif self.delta > self.deltatmax:
				heateroff()
				time.sleep(2)
				heateron()

		elif not hstat:
			if self.setpoint > curt:
				if self.setpoint - curt > self.undershoot:
					heateroff()

	def heateron(self):
		GPIO.output(self.pin,GPIO.HIGH)
		self.status = True
		self.lastshutoff = dattime.datetime.now()

	def heateroff(self):
		GPIO.output(self.pin,GPIO.LOW)
		self.status = False

	def getdeltat(self):
		a = datetime.datetime.now()
		dt = self.lastshutoff.seconds - a.seconds
		self.delta = dt

	def getstat(self):
		return self.status

	def setsetpoint(self,setpoint):
		self.setpoint =setpoint

	def setundert(self,undert):
		self.undershoot = undert

	def setovert(self,overt):
		self.overshoot = overt
