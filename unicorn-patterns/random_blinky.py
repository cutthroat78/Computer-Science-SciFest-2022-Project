#!/usr/bin/env python

import colorsys
import time
from sys import exit

try:
    import numpy
except ImportError:
    exit("This script requires the numpy module\nInstall with: sudo pip install numpy")

import unicornhat as unicorn

timeout = 20   # [seconds]

timeout_start = time.time()

unicorn.set_layout(unicorn.HAT)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()


while time.time() < timeout_start + timeout:
    rand_mat = numpy.random.rand(width,height)
    for y in range(height):
        for x in range(width):
            h = 0.1 * rand_mat[x, y]
            s = 0.8
            v = rand_mat[x, y]
            rgb = colorsys.hsv_to_rgb(h, s, v)
            r = int(rgb[0]*255.0)
            g = int(rgb[1]*255.0)
            b = int(rgb[2]*255.0)
            unicorn.set_pixel(x, y, r, g, b)
    unicorn.show()
    time.sleep(0.01)
