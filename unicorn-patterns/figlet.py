#!/usr/bin/env python

from time import sleep
from sys import exit
import time

try:
    from pyfiglet import figlet_format
except ImportError:
    exit("This script requires the pyfiglet module\nInstall with: sudo pip install pyfiglet")

import unicornhat as unicorn

timeout = 20   # [seconds]

timeout_start = time.time()

unicorn.set_layout(unicorn.HAT)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

TXT = "Scifest"

figletText = figlet_format(TXT+' ', "banner", width=1000) # banner font generates text with heigth 7
textMatrix = figletText.split("\n")[:width] # width should be 8 on both HAT and pHAT!
textWidth = len(textMatrix[0]) # the total length of the result from figlet
i = -1

def step():
    global i
    i = 0 if i>=100*textWidth else i+1 # avoid overflow
    for h in range(height):
        for w in range(width):
            hPos = (i+h) % textWidth
            chr = textMatrix[w][hPos]
            if chr == ' ':
                unicorn.set_pixel(width-w-1, h, 0, 0, 0)
            else:
                unicorn.set_pixel(width-w-1, h, 255, 0, 0)
    unicorn.show()

while time.time() < timeout_start + timeout:
    step()
    sleep(0.2)
