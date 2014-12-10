
#!/usr/bin/python

import sys
import datetime

from time import sleep
from datetime import datetime
from datetime import timedelta


_on = false

def Lights(on):
    if _on != on
        _on = on
        print "changed"
        return _on
    
    print "not changed"
    return _on


t = datetime.now()

for x in range(0,240):
    #print "value %d" % (x)
    d = datetime.now() - t
    print "the value %d and %d" % (d.seconds, Lights(d.seconds < 5))
    sleep(1)

#
#listen for device
#
#changed = current state != new state
#if changed
#    current state = new state
#    record time stamp
#
#if current state == present
#    Lights(current time - time stamp < 5)
#else
#    Lights(off)
#
#
#Lights(on)
#    if _on != on
#        _on = on
#        set lights to value
#
#
