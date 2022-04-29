#!/usr/bin/env python

import pyttsx3
import speech_recognition as sr
import webbrowser
import DateTime
import Wikipedia

answer = input("What is your answer?")

if answer == "candle":
	exec(open("unicorn-patterns/candle.py").read())
elif answer == "cross":
	exec(open("unicorn-patterns/cross.py").read())
