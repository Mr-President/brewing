#!/usr/bin/env python 
# -*- coding: utf-8 -*-

#Quick and dirty python implemenation of Servoblaster for the 
#Raspberry Pi, written by kols

#Servoblaster uses the BOARD numbering system. This means that if a servo is connected to BCM GPIO_5, Servoblaster is told to use BOARD pin 29

#Quick example showing how to write a script using this module. The example script is called servo_script.py, and the module is called servoblaster.py. They're both in the same directory

#import servoblaster
#import time
#servoblaster.initialize([29])
#servoblaster.position(0,100)
#time.sleep(1)
#servoblaster.position(0,150)
#time.sleep(0.5)
#servoblaster.stop()

###Actual module start

import subprocess

#Servoblaster install directory
#Example: "/home/pi/system/Pibits/ServoBlaster/"
install_dir = "/Home/Pibits/ServoBlaster/"

#Deafult values
idle_timeout = 1000 #Time before no pulse is sent to servo after last command, in milliseconds
initial_width = 140 #The initial position of the servo when initialized
#Max/min values are easy for one servo, but has to be implemented in the main script for more than one
#max_width = 2350
#min_width = 800

#Initialize the servo/servos. If you need max/min_width, then include them in the arguments (ex add max_width=max_width). Ex servoblaster.initialize([29]) or servoblaster.initialize([29],300,100) Must use brackets when initializing, even if you're only using one servo.
def initialize(servo_pins,idle_timeout=idle_timeout,initial_width=initial_width):
    pins = ','.join(map(str, servo_pins))
	
	#Here's what you're setting up servod with. Again, if max/min_width is needed, pass them here. Check servod --help to find out how
    servo_cmd = "%s/user/servod --p1pins=%s --idle-timeout=%dms" % (
        install_dir,pins,idle_timeout)
    
    subprocess.call(servo_cmd, shell=True)
    #for i in range(len(servo_pins)):
    #    subprocess.call("echo %d=%d > /dev/servoblaster" % (i,initial_width), shell=True)

#This function allows you to set the servo at a certain position. Default servo_n and pos are set, but when called, your own values are possible. Ex servoblaster.position(1,100) 
def position(servo_n=2,pos=initial_width):
        subprocess.call("echo %d=%d > /dev/servoblaster" % (servo_n,pos), shell=True)

#This function allows you to increment the servo position. Direction is altered with True/False. Default servo_n, direction and step-size are set, but when called, your own values are possible. Ex servoblaster.increment(0,False,5)
def increment(servo_n=2,direction=True,size=10):
    if direction is True:
        subprocess.call("echo %d=+%d > /dev/servoblaster" % (servo_n,size), shell=True)
    elif direction is False:
        subprocess.call("echo %d=-%d > /dev/servoblaster" % (servo_n,size), shell=True)

#This function terminates the servod instance, and should be executed when the main script has ended. Ex servoblaster.stop()
def stop():
    subprocess.call("killall servod" , shell=True)

