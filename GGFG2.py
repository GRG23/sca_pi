import random
import RPi.GPIO as GPIO
import time
random_number = random.randint(1,6) 
'n' = random.randint(1,6)
while True
    guess = int(raw_input("Guess an integer (between 1 and 10): "))

if guess < 'n':
        print 'Guess is too low'
        buzz_pin = 32
        GPIO.setmode (GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(buzz_pin,GPIO.OUT)
        Buzz = GPIO.PWM(buzz_pin,1000)
        Buzz. ChangeFrequency(440)
        Buzz.start(50)
        time.sleep(1)
        Buzz.stop()
        GPIO.cleanup()
 
else:
    if guess > 'n':
        print 'Guess is too high'
        buzz_pin = 32
        GPIO.setmode (GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(buzz_pin,GPIO.OUT)
        Buzz = GPIO.PWM(buzz_pin,1000)
        Buzz. ChangeFrequency(440)
        Buzz.start(50)
        time.sleep(1)
        Buzz.stop()
        GPIO.cleanup()

if guess == 'n':
    print 'You guessed it!'
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    led_pin = 11
    GPIO.setup(led_pin,GPIO.OUT)
    time.sleep(5)
    GPIO.output(led_pin, False)
    GPIO.cleanup()

