#!/bin/bash

#Global VARS:
device="C0:63:94:4E:62:F3"
btconnected=0
btcurrent=-1
counter=0
notconnected="0"
connected="1"
rssi=-1

state=0
newstate=0
changed=0


#Command loop:
while [ 1 ]; do


#cmdout=$(l2ping $device -c 1)
#btcurrent=$(echo $cmdout | grep -c "1 sent") 2> /dev/null

#echo $btcurrent
#i2cset -y 1 0x26 0

#if [ $btcurrent = $connected ]; then
#    i2cset -y 1 0x26 1
#fi
#sleep 1

#i2cset -y 1 0x26 0

#turn on red
i2cset -y 1 0x26 3

#listen for device
$changed=0
cmdout=$(l2ping $device -c 1)
btcurrent=$(echo $cmdout | grep -c "1 sent") 2> /dev/null

#clear all
i2cset -y 1 0x26 0

#get the connection state
$newstate=0
if [ $btcurrent = $connected ]; then
    $newstate=1
fi

#has the state changed
if [ $state -ne $newstate ]; then
    $state=$newstate
    $counter=0

    if [ $state = 1 ]; then
        $counter=10
    fi

    $changed=1
fi

if [ $counter -gt 0 ]; then
    ((counter--))
    if [ $counter = 0 ]; then
        $changed=1
    fi
fi

if [ $changed = 1 ]; then
    $changed=0

    if [ $counter -gt 0 ]; then
        i2cset -y 1 0x26 1
    fi

    if [ $counter = 0 ]; then
        i2cset -y 1 0x26 0
    fi
fi

sleep 5

#rssi=$(echo $cmdout | sed -e 's/RSSI return value: //g')

#if [ $btcurrent = $notconnected ]; then
#        echo "Attempting connection..."
#        rfcomm connect 0 $device 1 2> /dev/null >/dev/null &
#        sleep 1
#fi

#if [ $btcurrent = $connected ]; then
#        echo "Device connected. RSSI: "$rssi
#fi

#if [ $btconnected -ne $btcurrent ]; then
#        if [ $btcurrent -eq 0 ]; then
#                echo "GONE!"
#        fi
#        if [ $btcurrent -eq 1 ]; then
#                echo "HERE!"
#        fi
#        btconnected=$btcurrent
#fi

#sleep 1

done
