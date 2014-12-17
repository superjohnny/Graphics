
#!/usr/bin/env python2

import sys
import datetime
import subprocess
import math

from time import sleep
from datetime import datetime
from datetime import timedelta



class Device:
    id = "123"
    timestamp = datetime.now() - timedelta(0,10000)
    
    def __init__(self, id):
        self.id = id

    def SecondsSince(self):
        delta = datetime.now() - self.timestamp
        return delta.seconds




def GetMin(seq):
    def MinOf(x,y): return math.floor(x.SecondsSince(), y.SecondsSince())
    return reduce(MinOf, seq, 0)


def GetMinSeconds(arrayOfDevices):
    minTime = 32000
    for device in arrayOfDevices:
        dif = device.SecondsSince()
        if dif < minTime:
            minTime = dif

    return minTime


devices = [Device("xyz"), Device("lmn")]

#datetime(2014, 12, 15, 10, 0, 0, 0)

#devices[0].timestamp = datetime.now() - timedelta(0,2000)
#devices[1].timestamp = datetime.now() - timedelta(0,1000)

for device in devices:
    print "the device id = " + device.id + " seconds since = " + str(device.SecondsSince())


#y = GetMin(devices)
#print "the min time was " + str(y)

minTime = GetMinSeconds(devices)

print "the min time was " + str(minTime)

