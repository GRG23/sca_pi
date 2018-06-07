import random

i = 0

while i < 0:
    random_number = random.randint(1,4) 
    guessed_random_number = int(raw_input("Guess an integer (between 1 and 4): "))
i = i + 1
print random_number
if guessed_number != random_number: 
    print 'Your guess was correct'
