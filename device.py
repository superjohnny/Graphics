
#!/usr/bin/env python2

import sys
import datetime
import subprocess
import math

from time import sleep
from datetime import datetime
from datetime import timedelta



class Device:
    id = 0
    address = ""
    lastresponse = datetime.now() - timedelta(0,10000)
    status = 0

    def __init__(self, id, address, lastresponse, status):
        self.id = id
        self.address = address
        self.lastresponse = lastresponse
        self.status = status

    def SecondsSince(self):
        delta = datetime.now() - self.lastresponse
        return delta.seconds



def GetMinSeconds(arrayOfDevices):
    minTime = 32000
    for device in arrayOfDevices:
        dif = device.SecondsSince()
        if dif < minTime:
            minTime = dif

    return minTime



