
#!/usr/bin/env python2

import sys
import datetime
import subprocess
import math
import sqlite3
import random
import device
import hardwaredriver

from time import sleep
from datetime import datetime
from datetime import timedelta
from device import Device


def LoadDevices():

    devices = []

    #open database
    con = sqlite3.connect("devices.db", timeout=10)
    con.row_factory = sqlite3.Row
    
    #read into objects
    for row in con.execute("select * from device"):
        devices.append(Device(row["id"], row["address"], row["lastresponse"]))
    
    con.close()
    return devices


def UpdateDevice(device, timestamp):
    con = sqlite3.connect("devices.db", timeout=10)
    con.execute("update device set lastresponse = ? where id = ?", (timestamp, device.id,))
    con.commit()
    con.close()


while True:

    # load the list of devices to scan for
    devices = LoadDevices()
    
    for device in devices:
        # scan for each one
        if hardwaredriver.ReadBluetooth(device.address):
            # update time stamp for each discovered device
            delta = datetime.now() - device.lastresponse
            
            # only update if its been a while since the last time
            if (delta.seconds() < 230):
                UpdateDevice(device, datetime.now())
                print device.id


        else:
            # update time stamp to the past for each undiscovered device
            UpdateDevice(device, datetime.now() - timedelta(1,10000))
    






