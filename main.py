#!/usr/bin/env python

import os
import time
import speech_recognition as sr

# os.system('espeak -ven-us+f4 -s170 ""')

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

answer = input(">")# get_audio
print(answer)

if "display" in answer:
	if "candle" in answer:
		os.system('espeak -ven-us+f4 -s170 "Displaying a candle"')
		exec(open("unicorn-patterns/candle.py").read())
	elif "cross" in answer:
		exec(open("unicorn-patterns/cross.py").read())
		
elif "time" in answer:
	os.system('espeak -ven-us+f4 -s170 "It is $(date +"%l %M %p")"')

elif "date" in answer:
	os.system('espeak -ven-us+f4 -s170 "It is $(date +"%d") of $(date +"%B %Y")"')
