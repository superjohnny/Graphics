#Global VARS:
device="C0:63:94:4E:62:F3"
btconnected=0
btcurrent=-1
counter=0
notconnected="0"
connected="1"
rssi=-1
state=0

#Command loop:
#while [ 1 ]; do
i2cset -y 1 0x26 3

cmdout=$(l2ping $device -c 1)
btcurrent=$(echo $cmdout | grep -c "1 sent") 2> /dev/null

echo $btcurrent
i2cset -y 1 0x26 0

if [ $btcurrent = $connected ]; then
    i2cset -y 1 0x26 1
fi
sleep 1

i2cset -y 1 0x26 0

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

#done
