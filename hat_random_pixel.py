#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat ()
import random
import time
x = 1
while True:
    x < 10
    r = random.randint(0, 7)
    r2 = random.randint(0,7)
    c = random.randint(0, 255)
    c1= random.randint(0, 255)
    c2 = random.randint(0, 255)
    sense.set_pixel(r, r2, (c, c1, c2))
    time.sleep(5)
    x = x + 1

sense.clear()
