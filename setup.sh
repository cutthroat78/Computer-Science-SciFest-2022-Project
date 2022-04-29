#!/bin/bash
curl -sS https://get.pimoroni.com/unicornhat | bash # For Unicorn hat
sudo pip3 --no-cache-dir install SpeechRecognition playsound gtts pygobject pyaudio
sudo apt-get install python3-pyaudio python-pyaudio
