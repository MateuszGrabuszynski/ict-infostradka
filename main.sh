#!/bin/bash

# script should be running in the background

# reading from file (stack: 10929453)
#while IFS='' read -r line || [[ -n "$line" ]]; do
#    echo "Text read from file: $line"
#done < "$1"
# should be read from file
server_IP='192.168.1.100'
path='api/'
sleep_time=15 #screenshot every sleep_time seconds

while true; do
# screenshoting
scrot "screenshots/screenshot.jpg" --quality 15 --thumb 25 # path added for the screen to be always in the same place; check if you can screen thumbs only

# curling screenshots to the server_IP
#curl -T [ftp]

sleep $sleep_time
done
