
#!/usr/bin/python

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

    
#    print "not changed " + str(_on)
    return _on


#writes value to i2c command line
# 0 turns all off. 1 turns on green. 2 turns off green. 3 turns on red. 4 turns off red.
def WriteToDevice(value):
    
    try:
        subprocess.check_call("i2cset -y 1 0x26 " + str(value), shell=True)

    except:
        print "Error writing to device"

    return

# detects bluetooth presence of device with id
def ReadBluetooth(deviceid):
    response = False
    
    try:
        subprocess.check_output("l2ping " + deviceid + " -c 1 | grep -c '1 sent' 2> /dev/null", stderr=subprocess.STDOUT, shell=True)
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




#init
secondsBetweenScans = 1
secondsDurationOn = 10
timestamp = datetime.now()
deviceid = "C0:63:94:4E:62:F3"
state = False
_on = False



#loop
while True:
    #    newState = ReadBluetooth(deviceid)
    newState = ReadDummy()
    
    #has it changed
    if state != newState:
        state = newState
        timestamp = datetime.now()

    if state:
        delta = datetime.now() - timestamp
        Lights(delta.seconds < secondsDurationOn)
    else:
        Lights(False)

    sleep(secondsBetweenScans)


