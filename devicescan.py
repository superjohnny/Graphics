
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
    con.row_factory = sqlite3.Row #this encourages sqlite to use the timestamp type for the datetime columns on the way out
    
    #read into objects
    for row in con.execute("select * from device"):
        devices.append(Device(row["id"], row["address"], row["lastresponse"], row["status"]))
    
    con.close()
    return devices


def UpdateDevice(device, timestamp, status):
    con = sqlite3.connect("devices.db", timeout=10)
    con.execute("update device set lastresponse = ?, status = ? where id = ?", (timestamp, status, device.id,))
    con.commit()
    con.close()


while True:

    # load the list of devices to scan for
    devices = LoadDevices()
    
    for device in devices:
        # scan for each one
        if hardwaredriver.ReadBluetooth(device.address):
            
            #if the state has changed
            if device.status == 0:
                #update the timestamp and change the state
                UpdateDevice(device, datetime.now(), 1)
#                print "Updating device state " + device.address

            
            #if the state is the same
            #dont do anything
            
            
#            # update time stamp for each discovered device
#            delta = datetime.now() - device.lastresponse
#            
#            status = delta.seconds() < 230
#            
#            UpdateDevice(device, datetime.now(), status)
#            print device.id


        else:
            # update time stamp to the past for each undiscovered device
            UpdateDevice(device, datetime.now() - timedelta(1,10000), 0)
#            print "Device " + device.address + " not found"


        sleep(1)




