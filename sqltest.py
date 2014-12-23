
#!/usr/bin/env python2

import sys
import datetime
import subprocess
import sqlite3

from time import sleep
from datetime import datetime
from datetime import timedelta


con = sqlite3.connect("devices.db", timeout=10)
con.execute("create table if not exists device (id, address, lastresponse timestamp, status)")

devices = [(1, "ab:cd", datetime.now(),0), (2, "ef:gh", datetime.now(),0), (3, "ij:kl", datetime.now(),0),]

con.execute("delete from device")
con.commit()

con.executemany("insert into device values (?,?,?,?)", devices)
con.commit()

con.close()