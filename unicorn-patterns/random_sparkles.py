#!/usr/bin/env python

from random import randint

import time

import unicornhat as unicorn

timeout = 20   # [seconds]

timeout_start = time.time()

unicorn.set_layout(unicorn.HAT)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

while time.time() < timeout_start + timeout:
    x = randint(0, (width-1))
    y = randint(0, (height-1))
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    unicorn.set_pixel(x, y, r, g, b)
    unicorn.show()
