import sys
sys.path.append("/home/tupperbot/pibot/drivers/")
from sabertooth import *

if __name__ == "__main__":
	print "Let's weegle"
	MD = sabertoothSimplified()
	_delay = 0.2
	_speed = 100
	MD.wakeUp()
	
	MD.driveLeft(_speed)
	sleep(_delay)
	MD.driveRight(_speed)
	sleep(_delay)
	MD.driveLeft(_speed)
	sleep(_delay)
	MD.driveRight(_speed)
	sleep(_delay)
	
	MD.stop()
	