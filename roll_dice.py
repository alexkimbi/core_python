#!/usr/bin/python3
import random
roll = random.randint(1,6) # This will randomly roll any number b/w 1 and 6  
guess = int(input('Guess the dice roll:\n')) #Will work perfecrly if the guessed number matches with the random
if guess == roll:
    print("Correct! They rolled a " + str(roll))
else:
    print("Wrong! They rolled a " + str(roll))