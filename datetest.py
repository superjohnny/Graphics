
#!/usr/bin/python

import sys
import datetime

from time import sleep
from datetime import datetime
from datetime import timedelta


t = datetime.now()

for x in range(0,240):
    #print "value %d" % (x)
    d = datetime.now() - t
    print d.seconds
    sleep(1)
