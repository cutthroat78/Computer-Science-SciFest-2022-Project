#!/bin/bash
alsamixer # To change UX2's input to Microphone
cd /home/pi/Computer-Science-SciFest-2022-Project/zigbee/
docker-compose up -d
cd /home/pi/Computer-Science-SciFest-2022-Project/
sudo python3 main.py
