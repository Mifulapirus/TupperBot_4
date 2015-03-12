"""
 Title: maestro6.py
 Description: 
""" 
__author__ = "Angel Hernandez"
__contributors__ = "Angel Hernandez"
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Angel Hernandez"
__email__ = "angel@tupperbot.com"
__status__ = "beta"

import sys
sys.path.append("/home/tupperbot/pibot/drivers/")
from Maestro6 import *

class TB4:
	servo = maestro6('/dev/ttyACM0')
	
	def __init__(self, _port='/dev/ttyACM0'):
		self.head = 2
		self.left = 0
		self.right = 1
		self._leftDown = 3428
		self._rightDown = 8604
		self._headHome = 7500
		self._threshold = 10
		print "TupperBot 4 has been created"
		
	def home(self, turnOffWhenDone = False, acceleration=servo.defaultAccel, speed=servo.defaultSpeed):
		self.headHome(acceleration, speed)
		self.armDown(acceleration, speed)
		if (turnOffWhenDone):
			while (not(self._leftDown - self._threshold <= self.servo.getPosition(self.left) <= self._leftDown + self._threshold) or not(self._headHome - self._threshold <= self.servo.getPosition(head) <= self._headHome + self._threshold)):
				time.sleep(0.1)
			self.servo.servoOff(self.left)
			self.servo.servoOff(self.right)
			self.servo.servoOff(self.head)
	
	def allUp(self, acceleration=servo.defaultAccel, speed=servo.defaultSpeed):
		self.armUp(acceleration, speed)
		self.headUp(acceleration, speed)
	
	def armDownHeadUp(self, acceleration=servo.defaultAccel, speed=servo.defaultSpeed):
		self.servo.setPosition(self.left, self._leftDown+200)
		self.servo.setPosition(self.right,self._rightDown-200)
		self.servo.setPosition(self.head, 4400)
		
	def armUp(self, acceleration=servo.defaultAccel, speed=servo.defaultSpeed):
		self.servo.setPosition(self.left, 10000, acceleration, speed)
		self.servo.setPosition(self.right, 2000, acceleration, speed)
	
	def armDown(self, acceleration=servo.defaultAccel, speed=servo.defaultSpeed):
		self.servo.setPosition(self.left, self._leftDown, acceleration, speed)
		self.servo.setPosition(self.right, self._rightDown, acceleration, speed)
	
	def headUp(self, acceleration=servo.defaultAccel, speed=servo.defaultSpeed):
		self.servo.setPosition(self.head, 3500, acceleration, speed)
	
	def headDown(self, acceleration=servo.defaultAccel, speed=servo.defaultSpeed):
		self.servo.setPosition(self.head, 8000, acceleration, speed)
	
	def headHome(self, acceleration=servo.defaultAccel, speed=servo.defaultSpeed):
		self.servo.setPosition(self.head, self._headHome, acceleration, speed)