#!/usr/bin/env python

import os, sys, time, random
import speech_recognition as sr

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

# os.system('espeak -ven-us+f4 -s170 "Say something for me to do"')
answer = sys.argv[1]
#answer = get_audio()
print(answer)

if "display" in answer:
	if "random" in answer:
		choices = ["unicorn-patterns/candle.py", "unicorn-patterns/cross.py", "unicorn-patterns/demo.py", "unicorn-patterns/drop_four_orientation.py", "unicorn-patterns/drop.py", "unicorn-patterns/figlet.py", "unicorn-patterns/matrix.py", "unicorn-patterns/rainbow_blinky.py", "unicorn-patterns/rainbow.py", "unicorn-patterns/random_blinky.py", "unicorn-patterns/random_sparkles.py", "unicorn-patterns/simple.py", "unicorn-patterns/snow.py"]
		os.system('espeak -ven-us+f4 -s170 "Displaying a random pattern"')
		exec(open(random.choice(choices)).read())
	elif "candle" in answer:
		os.system('espeak -ven-us+f4 -s170 "Displaying a candle"')
		exec(open("unicorn-patterns/candle.py").read())
	elif "shooting" in answer:
		os.system('espeak -ven-us+f4 -s170 "Displaying shooting stars"')
		exec(open("unicorn-patterns/cross.py").read())
	elif "demo" in answer:
		os.system('espeak -ven-us+f4 -s170 "Displaying demo pattern"')
		exec(open("unicorn-patterns/demo.py").read())
	elif "drop one" in answer:
		os.system('espeak -ven-us+f4 -s170 "Displaying drop pattern one"')
		exec(open("unicorn-patterns/drop_four_orientation.py").read())
	elif "drop two" in answer:
		os.system('espeak -ven-us+f4 -s170 "Displaying drop pattern two"')
		exec(open("unicorn-patterns/drop.py").read())
	elif "text" in answer:
		os.system('espeak -ven-us+f4 -s170 "Displaying text"')
		exec(open("unicorn-patterns/figlet.py").read())
	elif "matrix" in answer:
		os.system('espeak -ven-us+f4 -s170 "Displaying the matrix"')
		exec(open("unicorn-patterns/matrix.py").read())
	elif "rainbow one" in answer:
		os.system('espeak -ven-us+f4 -s170 "Displaying rainbow pattern one"')
		exec(open("unicorn-patterns/rainbow.py").read())
	elif "rainbow two" in answer:
		os.system('espeak -ven-us+f4 -s170 "Displaying rainbow pattern two"')
		exec(open("unicorn-patterns/rainbow.py").read())
	elif "speedy" in answer:
		os.system('espeak -ven-us+f4 -s170 "Displaying a speedy pattern"')
		exec(open("unicorn-patterns/random_blinky.py").read())
	elif "sparkles" in answer:
		os.system('espeak -ven-us+f4 -s170 "Displaying sparkles"')
		exec(open("unicorn-patterns/random_sparkles.py").read())
	elif "fill" in answer:
		os.system('espeak -ven-us+f4 -s170 "Displaying filling the jar one by one pattern"')
		exec(open("unicorn-patterns/simple.py").read())
	elif "snow" in answer:
		os.system('espeak -ven-us+f4 -s170 "Displaying snow"')
		exec(open("unicorn-patterns/snow.py").read
		
if "turn" in answer or "light":
	if "on" in answer:
		os.system('espeak -ven-us+f4 -s170 "Turning on the light bulb"')
		# To Do
	elif "off" in answer:
		os.system('espeak -ven-us+f4 -s170 "Turning off the light bulb"')
		# To Do
				
elif "time" in answer:
	os.system('espeak -ven-us+f4 -s170 "It is $(date +"%l %M %p")"')

elif "date" in answer:
	os.system('espeak -ven-us+f4 -s170 "It is $(date +"%d") of $(date +"%B %Y")"')
	
	
elif "say" in answer or "something" in answer:
	os.system('espeak -ven-us+f4 -s170 "What would you like me to say?"')
	say_something = '"' + input(">") + '"'
	os.system('espeak -ven-us+f4 -s170 ' + say_something)
	
elif "hello" in answer or "hi" in answer:
	number = random.randint(0,2)
	if number == 1:
		os.system('espeak -ven-us+f4 -s170 "Hello, human"')
	elif number == 2:
		os.system('espeak -ven-us+f4 -s170 "Hi"')

