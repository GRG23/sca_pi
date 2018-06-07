#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()

# use RGB values to define colours
yellow = (255, 255, 0)
blue = (0, 0, 255)

speed = 0.05

message "Hello World!"

sense.show_message(message, speed, text_color=yellow, back_colour=blue)

sense.clear()
