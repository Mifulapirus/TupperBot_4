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
import sabertooth
from time import sleep

class TB4:
	servo = maestro6('/dev/ttyACM0')
	MD = sabertooth.sabertoothSimplified()
	
	def __init__(self, _port='/dev/ttyACM0'):
		self.head = 2
		self.left = 0
		self.right = 1
		self._leftDown = 3428
		self._leftUp = 6848
		
		self._rightDown = 8604
		self._rightUp = 4928
		
		self._headUp = 3200
		self._headDown = 10048
		
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
	
	def relax(self, acceleration=servo.defaultAccel, speed=servo.defaultSpeed):
		self.headPosition(15)
		self.armPosition(60)
	
	#position in %
	def armPosition(self, position, acceleration=servo.defaultAccel, speed=servo.defaultSpeed):
		if position > 100: position = 100
		elif position < 0: position = 0
		_leftFactor = abs(self._leftDown - self._leftUp) / 100.0
		_rightFactor = abs(self._rightDown - self._rightUp) / 100.0
		
		_leftPos = self._leftDown + int(position * _leftFactor)
		_rightPos = self._rightDown - int(position * _rightFactor)
		
		self.servo.setPosition(self.left, _leftPos, acceleration, speed)
		self.servo.setPosition(self.right, _rightPos, acceleration, speed)
	
	#position in %
	def headPosition(self, position, acceleration=servo.defaultAccel, speed=servo.defaultSpeed):
		if position > 100: position = 100
		elif position < 0: position = 0
		_factor = abs(self._headDown - self._headUp) / 100.0
				
		_pos = self._headUp + int(position * _factor)
				
		self.servo.setPosition(self.head, _pos)
			
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
	
	def wiggle(self, _delay = 0.2, _speed = 100):
		self.MD.wakeUp()
		
		self.MD.driveLeft(_speed)
		sleep(_delay)
		self.MD.driveRight(_speed)
		sleep(_delay)
		self.MD.driveLeft(_speed)
		sleep(_delay)
		self.MD.driveRight(_speed)
		sleep(_delay)
		
		self.MD.stop()