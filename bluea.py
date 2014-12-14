
#!/usr/bin/python

import sys
import subprocess

from time import sleep

subprocess.check_call("i2cset -y 1 0x26 0", shell=True)
subprocess.check_call("i2cset -y 1 0x26 1", shell=True)

response = 0

try:
    subprocess.check_output("l2ping C0:63:94:4E:62:F3 -c 1 | grep -c '1 sent' 2> /dev/null", stderr=subprocess.STDOUT, shell=True)
    response = 1

except:
    response = 0

print('the value was: ', response)

subprocess.check_call("i2cset -y 1 0x26 0", shell=True)

if response == 1:
    subprocess.check_call("i2cset -y 1 0x26 1", shell=True)
else:
    subprocess.check_call("i2cset -y 1 0x26 3", shell=True)

