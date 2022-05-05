#!/usr/bin/env python3

import os, sys, time, random, wikipedia, randfacts, pyjokes
from PyDictionary import PyDictionary
import speech_recognition as sr

dictionary=PyDictionary()
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
	
def speak(phrase):
	quoted = '"' + phrase + '"'
	os.system('espeak ' + quoted + " --stdout | aplay -D sysdefault")

#answer = sys.argv[1]
while True:
	speak("I am listening now")
	print("Listening")
	answer = get_audio()
	print(answer)

	if "play" in answer or "show" in answer:
		if "random" in answer:
			choices = ["unicorn-patterns/candle.py", "unicorn-patterns/cross.py", "unicorn-patterns/demo.py", "unicorn-patterns/drop_four_orientation.py", "unicorn-patterns/drop.py", "unicorn-patterns/figlet.py", "unicorn-patterns/matrix.py", "unicorn-patterns/rainbow_blinky.py", "unicorn-patterns/rainbow.py", "unicorn-patterns/random_blinky.py", "unicorn-patterns/random_sparkles.py", "unicorn-patterns/simple.py", "unicorn-patterns/snow.py"]
			speak("Displaying a random pattern")
			exec(open(random.choice(choices)).read())
		elif "candle" in answer:
			speak("Displaying a candle")
			exec(open("unicorn-patterns/candle.py").read())
		elif "shooting" in answer or "star" in answer:
			speak("Displaying shooting stars")
			exec(open("unicorn-patterns/cross.py").read())
		elif "demo" in answer:
			speak("Displaying demo pattern")
			exec(open("unicorn-patterns/demo.py").read())
		elif "drop one" in answer:
			speak("Displaying drop pattern one")
			exec(open("unicorn-patterns/drop_four_orientation.py").read())
		elif "drop two" in answer:
			speak("Displaying drop pattern two")
			exec(open("unicorn-patterns/drop.py").read())
		elif "text" in answer:
			speak("Displaying text")
			exec(open("unicorn-patterns/figlet.py").read())
		elif "matrix" in answer or "Matrix" in answer:
			speak("Displaying the matrix")
			exec(open("unicorn-patterns/matrix.py").read())
		elif "rainbow" in answer or "Rainbow" in answer:
			speak("Displaying a rainbow")
			exec(open("unicorn-patterns/rainbow.py").read())
		elif "blink" in answer:
			speak("Displaying blink")
			exec(open("unicorn-patterns/rainbow.py").read())
		elif "blink 2" in answer:
			speak("Displaying blink 2")
			exec(open("unicorn-patterns/random_blinky.py").read())
		elif "sparkles" in answer:
			speak("Displaying sparkles")
			exec(open("unicorn-patterns/random_sparkles.py").read())
		elif "fill" in answer:
			speak("Displaying filling the jar one by one pattern")
			exec(open("unicorn-patterns/simple.py").read())
		elif "snow" in answer:
			speak("Displaying snow")
			exec(open("unicorn-patterns/snow.py").read())
		elif "display" in answer:
			speak("I dont know a pattern called " + answer[8:])
		elif "play" in answer or "show" in answer:
			speak("I dont know a pattern called " + answer[5:])
			
	elif "who made" in answer or "who created" in answer:
		speak("I was made by Iustina, Cathal and Matthew from Clogher Road Community College")
		
	elif "define the word" in answer:
		speak(str(dictionary.meaning(answer[16:])))
			
	elif "define" in answer:
		speak(str(dictionary.meaning(answer[7:])))
	
	elif "what is the meaning of the word" in answer:
		speak(str(dictionary.meaning(answer[32:])))
		
	elif "turn" in answer or "light" in answer:
		if "on" in answer:
			speak("Turning on the light bulb")
			# To Do
		elif "off" in answer:
			speak("Turning off the light bulb")
			# To Do	
		else:
			speak("I didnt understand what you meant by " + answer)	
		
	elif "time" in answer:
		os.system('espeak "It is $(date +"%l %M %p")" --stdout | aplay -D sysdefault')
	
	elif "date" in answer:
		os.system('espeak "It is $(date +"%d") of $(date +"%B %Y")" --stdout | aplay -D sysdefault')
	
	elif "say" in answer:
		speak(answer[4:])
	
	elif "hello" in answer or "hi" in answer:
		number = random.randint(1,2)
		if number == 1:
			speak("Hello, human")
		elif number == 2:
			speak("Hi")
			
	elif "good morning" in answer:
		speak("Good morning")
		
	elif "good day" in answer:
		speak("Good day")
		
	elif "good evening" in answer:
		speak("Good evening")
		
	elif "good afternoon" in answer:
		speak("Good afternoon")
		
	elif "good night" in answer or "goodnight" in answer:
		speak("Good night")
		
	elif "goodbye" in answer or "good bye" in answer or "bye" in answer:
		speak("Good bye")
		
	elif "what is" in answer:
		search = '"' + answer[8:] + '"'
		wiki = "'" + wikipedia.summary(search) + "'"
		print(wiki)
		speak(wiki)
		
	elif "who is" in answer:
		search = '"' + answer[7:] + '"'
		wiki = "'" + wikipedia.summary(search) + "'"
		print(wiki)
		speak(wiki)
		
	elif "wikipedia" in answer or "Wikipedia" in answer:
		search = '"' + answer[10:] + '"'
		wiki = "'" + wikipedia.summary(search) + "'"
		print(wiki)
		speak(wiki)
		
	elif "wiki" in answer or "Wiki" in answer:
		search = '"' + answer[5:] + '"'
		wiki = "'" + wikipedia.summary(search) + "'"
		print(wiki)
		speak(wiki)
		
	elif not answer:
		number = random.randint(1,2)
		if number == 1:
			speak("Is anybody there?")
		elif number == 2:
			speak("I can't hear you!")
			
	elif "ass" in answer or "*" in answer or "dick" in answer:
		number = random.randint(1,2)
		if number == 1:
			speak("Don't use such language!")
		elif number == 2:
			speak("Don't curse at me!")
			
	elif "how are you" in answer:
		number = random.randint(1,3)
		if number == 1:
			speak("I am fine")
		elif number == 2:
			speak("I am good")
		elif number == 3:
			speak("I don't know, I can't feel")
			
	elif "how is your day" in answer:
		speak("My day is going well")
		
	elif "fact" in answer:
		fact = randfacts.get_fact()
		print(fact)
		speak(fact)
		
	elif "joke" in answer:
		joke = pyjokes.get_joke()
		print(joke)
		speak(joke)
		
	else:
		speak("I didnt understand what you meant by " + answer)
