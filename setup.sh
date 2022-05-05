#!/bin/bash
sudo apt update
curl -sS https://get.pimoroni.com/unicornhat | bash # For Unicorn hat
sudo apt-get install python3-pyaudio python-pyaudio espeak flac
sudo pip3 --no-cache-dir install pyjokes SpeechRecognition pyaudio pyfiglet wikipedia PyDictionary randfacts
curl -fsSL https://get.docker.com -o get-docker.sh # Get docker install script
sudo sh get-docker.sh # Install docker using script
sudo pip3 install docker-compose # Install docker-compose for quick deployment of zigbee stuff
sudo systemctl enable docker # Have docker start on system start up
sudo chmod +x *.sh 
sudo apt-key adv --keyserver hkps://keyserver.ubuntu.com:443 --recv-keys 04EE7237B7D453EC 648ACFD622F3D138 # This command and below 3 command needed to make zigbe2mqtt to work on raspbian buster
echo "deb http://httpredir.debian.org/debian buster-backports main contrib non-free" | sudo tee -a "/etc/apt/sources.list.d/debian-backports.list"
sudo apt update
sudo apt install libseccomp2 -t buster-backports
