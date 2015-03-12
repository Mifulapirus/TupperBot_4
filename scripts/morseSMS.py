import sys
sys.path.append("/home/tupperbot/pibot/drivers/")
from TB4_driver import *
import emailChecker

TupperBot = TB4()
correo = emailChecker.emailChecker(_user = 'mail@gmail.com', _pass = '1234')
beatDelay = 0.08
dotDelay = 0.2
lineDelay = 0.6


def dot():
	TupperBot.armPosition(15, 0, 0)
	sleep(beatDelay)
	#down
	TupperBot.armPosition(8, 0, 0)
	sleep(beatDelay)
	

def line():
	TupperBot.armPosition(13, 0, 0)
	sleep(beatDelay*4)
	#down
	TupperBot.armPosition(8, 0, 0)
	sleep(beatDelay*5)
	
def morseSMS():
	dot()
	dot()
	dot()
	line()
	line()
	dot()
	dot()
	dot()

if __name__ == "__main__":
	while True:
		if (correo.checkIfNewEmail()):
			TupperBot.home()
			sleep(0.2)
			TupperBot.MD.driveForward(50)
			sleep(0.1)
			TupperBot.MD.driveForward(50)
			sleep(0.1)
			TupperBot.MD.driveForward(50)
			sleep(0.5)
			TupperBot.MD.stop()
			TupperBot.armDownHeadUp()
			time.sleep(2)
	
			morseSMS()
			TupperBot.MD.driveBackwards(50)
			sleep(0.1)
			TupperBot.home()
			TupperBot.MD.driveBackwards(50)
			sleep(0.1)
			TupperBot.home()
			TupperBot.MD.driveBackwards(50)
			sleep(0.5)
			
			time.sleep(3)
			
			TupperBot.servo.servoOff(TupperBot.left)
			TupperBot.servo.servoOff(TupperBot.right)
			TupperBot.servo.servoOff(TupperBot.head)
		else:
			sleep(2)
	
	