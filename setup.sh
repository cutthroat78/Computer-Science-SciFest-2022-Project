#!/bin/bash
curl -sS https://get.pimoroni.com/unicornhat | bash # For Unicorn hat
sudo apt-get install python3-pyaudio python-pyaudio espeak flac
sudo pip3 --no-cache-dir install SpeechRecognition pyaudio pyfiglet
curl -fsSL https://get.docker.com -o get-docker.sh # Get docker install script
sudo sh get-docker.sh # Install docker using script
sudo pip3 install docker-compose # Install docker-compose for quick deployment of zigbee stuff
sudo systemctl enable docker # Have docker start on system start up
