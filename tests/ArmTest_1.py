import sys
sys.path.append("/home/tupperbot/pibot/drivers/")
from Maestro6 import *

if __name__ == "__main__":
	head = 2
	left = 0
	right = 1
	_leftDown = 3428
	_rightDown = 8604
	_headHome = 7500
	_threshold = 10
	servo = maestro6('/dev/ttyACM0')
	
	def home(turnOffWhenDone = False):
		headHome()
		armDown()
		if (turnOffWhenDone):
			while (not(_leftDown - _threshold <= servo.getPosition(left) <= _leftDown + _threshold) or not(_headHome - _threshold <= servo.getPosition(head) <= _headHome + _threshold)):
				time.sleep(0.1)
			servo.servoOff(left)
			servo.servoOff(right)
			servo.servoOff(head)
			

	
	def allUp():
		armUp()
		headUp()
	
	def armDownHeadUp():
		servo.setPosition(left, _leftDown+200)
		servo.setPosition(right, _rightDown-200)
		servo.setPosition(head, 4400)
		
	def armUp():
		servo.setPosition(left, 10000)
		servo.setPosition(right, 2000)
	
	def armDown():
		servo.setPosition(left, _leftDown)
		servo.setPosition(right, _rightDown)
	
	def headUp(acceleration=servo.DEFAULT_ACCEL, speed=servo.DEFAULT_SPEED):
		servo.setPosition(head, 3500, acceleration, speed)
	
	def headDown(acceleration=servo.DEFAULT_ACCEL, speed=servo.DEFAULT_SPEED):
		servo.setPosition(head, 8000, acceleration, speed)
	
	def headHome(acceleration=servo.DEFAULT_ACCEL, speed=servo.DEFAULT_SPEED):
		servo.setPosition(head, _headHome, acceleration, speed)
	
	while 1:
		home()
		time.sleep(5)
		armDownHeadUp()
		time.sleep(5)
		
		allUp()
		time.sleep(2)
		headDown(40,0)
		time.sleep(0.5)
		headUp(40,0)
		time.sleep(0.5)
		headDown(40,0)
		time.sleep(0.5)
		headUp(40,0)
		time.sleep(0.5)
		
		allUp()
		time.sleep(3)