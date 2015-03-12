import sys
sys.path.append("/home/tupperbot/pibot/drivers/")
from sabertooth import *

if __name__ == "__main__":
	MD = sabertooth()
	_delay = 3
	MD.driveMixedStart()
	print "Wheel test"
	
	while 1:
		
		MD.driveForward(10)
		sleep(_delay)
		MD.stop()
		sleep(_delay)
		
		MD.driveBackwards(20)
		sleep(_delay)
		MD.stop()
		sleep(_delay)