import sys
sys.path.append("/home/tupperbot/pibot/drivers/")
from TB4_driver import *

if __name__ == "__main__":
	TupperBot = TB4()
	TupperBot.home()
	time.sleep(1)
	TupperBot.armDownHeadUp()
	time.sleep(2)
	TupperBot.servo.servoOff(TupperBot.left)
	TupperBot.servo.servoOff(TupperBot.right)
	TupperBot.servo.servoOff(TupperBot.head)