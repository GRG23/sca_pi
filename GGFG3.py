import random
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

buzz_pin = 32
led_pin = 11

GPIO.setup(buzz_pin,GPIO.OUT)

Buzz = GPIO.PWM(buzz_pin,1000)


def buzz (freq):
    Buzz.ChangeFrequency(freq)
    Buzz.start(50)
    time.sleep(1)
    Buzz.stop()
n = 2
while True:
    n = int(raw_input("Guess an integer (between 1 and 10): "))

    if n < 2:
        print 'Guess is too low'
        buzz(440)
    elif n > 2:
        print 'Guess is too high'
        buzz(880)
    else:
        print 'You guessed it!'
        GPIO.output(led_pin, True)
        time.sleep(5)
        GPIO.output(led_pin, False)
        GPIO.cleanup()
