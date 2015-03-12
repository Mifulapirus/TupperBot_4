import sys
sys.path.append("/home/tupperbot/pibot/drivers/")
from TB4_driver import *

if __name__ == "__main__":
	TupperBot = TB4()
	
	TupperBot.home(False, 4,20)
	time.sleep(1)
		
	TupperBot.allUp(8, 20)
	time.sleep(2)
	TupperBot.headDown(0,80)
	time.sleep(0.5)
	TupperBot.headUp(0,80)
	time.sleep(0.5)
	TupperBot.headDown(0,80)
	time.sleep(0.5)
	TupperBot.headUp(0,80)
	time.sleep(0.5)
	
	TupperBot.wiggle()
	
	TupperBot.relax()
	time.sleep(2)
	TupperBot.servo.servoOff(TupperBot.left)
	TupperBot.servo.servoOff(TupperBot.right)
	TupperBot.servo.servoOff(TupperBot.head)