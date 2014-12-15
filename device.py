
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
    timestamp = datetime.now()
    
    def __init__(self, id):
        self.id = id

    def SecondsSince(self):
        delta = datetime.now() - self.timestamp
        return delta.seconds




def GetMin(seq):
    def MinOf(x,y): return math.floor(x.SecondsSince(), y.SecondsSince())
    return reduce(MinOf, seq, 0)


devices = [Device("xyz"), Device("lmn")]

#datetime(2014, 12, 15, 10, 0, 0, 0)

devices[0].timestamp = datetime.now() - timedelta(0,20)
devices[1].timestamp = datetime.now() - timedelta(0,10)

for device in devices:
    print "the device id = " + device.id + " seconds since = " + str(device.SecondsSince())


minTime = 32000
for device in devices:
    dif = device.SecondsSince()
    if dif < minTime:
        minTime = dif

print "the min time was " + str(minTime)

