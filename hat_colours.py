#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()

# use RGB values to define colours
random = (76, 89, 123)
random2 = (78, 78, 98)

speed = 0.05

message = "Ur Sister A Mister"

sense.show_message(message, speed, text_colour=random, back_colour=random2)

sense.clear()
