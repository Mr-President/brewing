#heater class will contain the object heater where the status and the processs of setting the heater output will be contained
import RPi.GPIO as GPIO
import time
import datetime


class Heater:

	def __init__(self, pin, temp,setp,undert,overt,tdmax = 60, status = False):
		self.pin = pin
		self.status = status
		self.temperature = temp
		self.setpoint = setp
		self.undershoot = undert
		self.overshoot = overt
		self.deltatmax = tdmax
		self.lastshutoff = datetime.datetime.now()
		self.delta = 0
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.pin, GPIO.OUT)

	def heateron(self):
		GPIO.output(self.pin,GPIO.HIGH)
		self.status = True
		self.lastshutoff = datetime.datetime.now()

	def heateroff(self):
		GPIO.output(self.pin,GPIO.LOW)
		self.status = False

	def getstat(self):
		return self.status

	def setsetpoint(self,setpoint):
		self.setpoint =setpoint

	def setundert(self,undert):
		self.undershoot = undert

	def setovert(self,overt):
		self.overshoot = overt
		
	def update(self,curt):
		a = datetime.datetime.now()
		dt = a - self.lastshutoff
		delt = divmod(dt.seconds,60)
		self.delta = delt[0]
		if self.status:
			if curt > self.setpoint:
				if curt - self.setpoint > self.overshoot:
					self.heateroff()
			elif self.delta > self.deltatmax:
				self.heateroff()
				print "power cycle"
				time.sleep(2)
				self.heateron()
			else:
				pass

		elif not self.status:
			if self.setpoint > curt:
				if self.setpoint - curt > self.undershoot:
					self.heateron()

