#!/bin/bash
alsamixer # To change UX2's input to Microphone
cd /home/pi/Computer-Science-SciFest-2022-Project/zigbee/
sudo docker-compose up -d
cd /home/pi/Computer-Science-SciFest-2022-Project/
pavucontrol &
sudo python3 main.py
