#!/usr/bin/env python

import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "./voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""

		try:
		    said = r.recognize_google(audio)
		    print(said)
		except Exception as e:
		    print("Exception: " + str(e))

	return said

answer = input("Answer:")# get_audio()

if "candle" in answer:
	speak("Displaying a candle")
	exec(open("unicorn-patterns/candle.py").read())
elif "cross" in answer:
	exec(open("unicorn-patterns/cross.py").read())

if "display candle" in answer:
	exec(open("unicorn-patterns/candle.py").read())
elif "display cross" in answer:
	exec(open("unicorn-patterns/cross.py").read())
