
#!/usr/bin/env python2

import sys
import subprocess


# writes value to i2c command line
# 0 turns all off. 1 turns on main. 2 turns off main. 3 turns on red. 4 turns off red. 5 turns on green. 6 turns off green.
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


