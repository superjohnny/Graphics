
#!/usr/bin/env python2

import sys
import datetime
import subprocess
import math
import sqlite3
import device
import hardwaredriver

from time import sleep
from datetime import datetime
from datetime import timedelta
from device import Device


def Lights(on):
    global _on
    
    if _on != on:
        _on = on

        #write to device
        if _on:
            hardwaredriver.WriteToDevice(1,0)
        else:
            hardwaredriver.WriteToDevice(2,0)

    return _on


def GetMostRecentDevice():
    # get the most recent device from the database
    con = sqlite3.connect("devices.db", detect_types=sqlite3.PARSE_DECLTYPES, timeout=10)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from device order by lastresponse desc limit 1")
    row = cur.fetchone()
    device = Device(row["id"], row["address"], row["lastresponse"])
    con.close()
    return device




#init
fastScans = 3
slowScans = 15
secondsBetweenScans = fastScans
secondsDurationOn = 250
_on = False


hardwaredriver.WriteToDevice(1,0)
hardwaredriver.WriteToDevice(0,0)
hardwaredriver.WriteToDevice(3,0)
hardwaredriver.WriteToDevice(0,0)


while True:

    device = GetMostRecentDevice()
    
    print device.SecondsSince()
    Lights(device.SecondsSince() < secondsDurationOn)
    
    sleep(secondsBetweenScans)




