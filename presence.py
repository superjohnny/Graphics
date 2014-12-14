
#!/usr/bin/env python2

import sys
import datetime
import subprocess

from time import sleep
from datetime import datetime
from datetime import timedelta


def Lights(on):
    global _on
    if _on != on:
        _on = on
        print "changed " + str(_on)
        #write to device
        if _on:
            WriteToDevice(1,0)
        else:
            WriteToDevice(2,0)
    
#    print "not changed " + str(_on)
    return _on


# writes value to i2c command line
# 0 turns all off. 1 turns on green. 2 turns off green. 3 turns on red. 4 turns off red.
def WriteToDevice(value, retry):
    
    if retry > 3:
        return

    try:
        subprocess.check_call("i2cset -y 1 0x26 " + str(value), shell=True)

    except:
        print "Error writing to device " + str(value)
	WriteToDevice(value, retry + 1)
	
    return

# detects bluetooth presence of device with id
def ReadBluetooth(deviceid):
    response = False
    
    try:
        subprocess.check_output("l2ping " + deviceid + " -c 2 | grep -c 'sent' 2> /dev/null", stderr=subprocess.STDOUT, shell=True)
        response = True
    
    except:
        response = False

    return response



# dummy version of ReadBluetooth
_dummy = datetime.now()
def ReadDummy():
    global _dummy
    delta = datetime.now() - _dummy
    return delta.seconds > 5 and delta.seconds < 30


# Or's the elements of an array together
def OrElements(seq):
    def OrPair(x,y): return x or y
    return reduce(OrPair, seq, 0)


#init
fastScans = 3
slowScans = 15
secondsBetweenScans = fastScans
secondsDurationOn = 250
timestamp = datetime.now()
#deviceids = ["C0:63:94:4E:62:F3", "C0:63:94:4E:62:F1"]
deviceids = ["CD:63:94:4E:62:F3"]
state = False
_on = False


WriteToDevice(1,0)
WriteToDevice(0,0)
WriteToDevice(3,0)
WriteToDevice(0,0)

#loop
while True:
    #    newState = ReadBluetooth(deviceid)
    #newState = ReadDummy()

    #scan for devices
    for device in deviceids:
        WriteToDevice(3,0)
        print "scanning for " + device
        newState = False
        deviceState = ReadBluetooth(device)
        if deviceState:
            # if any device found, set for True
            print "found " + device		
            newState = True
            break

    WriteToDevice(4,0)

    #has it changed
    if state != newState:
        state = newState
        timestamp = datetime.now()

    if state:
        delta = datetime.now() - timestamp
        Lights(delta.seconds < secondsDurationOn)
        secondsBetweenScans = slowScans
    else:
        Lights(False)
        secondsBetweenScans = fastScans

    print "sleeping for " + str(secondsBetweenScans)
    sleep(secondsBetweenScans)



