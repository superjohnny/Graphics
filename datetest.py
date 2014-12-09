
#!/usr/bin/python

import sys
import datetime

from time import sleep
from datetime import datetime
from datetime import timedelta


def Lights(theValue):
    return theValue < 5


t = datetime.now()

for x in range(0,240):
    #print "value %d" % (x)
    d = datetime.now() - t
    print "the value %d and %d" % (d.seconds, Lights(d.seconds))
    sleep(1)


