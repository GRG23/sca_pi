#!/usr/bin/env python
from sense_hat import SenseHat
import time
import random
sense = SenseHat()

r = random.randint(0, 255)
r1 = random.randint(0, 255)
r2 = random.randint(0, 255)

sense.show_letter("H", (r, r1, r2))
time.sleep(1)
sense.show_letter("i", (r1, r, r2))
time.sleep(1)

sense.show_letter("!", (r2, r1, r))
time.sleep(1)

sense.clear()
