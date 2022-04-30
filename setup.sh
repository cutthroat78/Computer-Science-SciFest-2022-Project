#!/bin/bash
curl -sS https://get.pimoroni.com/unicornhat | bash # For Unicorn hat
sudo apt-get install python3-pyaudio python-pyaudio espeak ansiweather
sudo pip3 --no-cache-dir install SpeechRecognition pyaudio pyfiglet
