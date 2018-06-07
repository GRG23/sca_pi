import random

n = 2
while True:
    n = int(raw_input("Guess an integer (between 1 and 10): "))

    if n < 2:
        print 'Guess is too low'

    elif n > 2:
         print 'Guess is too high'

    else:
        print 'You guessed it!'
