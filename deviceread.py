
#!/usr/bin/env python2

import sys
import datetime
import subprocess
import math
import sqlite3
import device

from time import sleep
from datetime import datetime
from datetime import timedelta
from device import Device

while True:

    # get the most recent device from the database
    con = sqlite3.connect("devices.db", detect_types=sqlite3.PARSE_DECLTYPES, timeout=10)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from device order by lastresponse desc limit 1")
    row = cur.fetchone()
    device = Device(row["id"], row["address"], row["lastresponse"])
    con.close()
    
    
    print device.SecondsSince()

    sleep(5)




