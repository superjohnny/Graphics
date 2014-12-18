
#!/usr/bin/env python2

import sys
import datetime
import subprocess
import math
import sqlite3
import random
import device

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


def UpdateDevice(device):
    con = sqlite3.connect("devices.db", timeout=10)
    con.execute("update device set lastresponse = ? where id = ?", (datetime.now(), device.id,))
    con.commit()
    con.close()


while True:

    # load the list of devices to scan for
    devices = LoadDevices()
    
    # scan for each one
    
    # update time stamp for each discovered device
    index = random.randint(0,2)
    device = devices[index]
    print device.id
    UpdateDevice(device)

    sleep(5)




