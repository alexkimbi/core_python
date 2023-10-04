#!/usr/bin/python3
import random

computer_choice = random.choice(['rock','paper','scissors']) # This is a list where the random will choose from by auto
# and matches the condition in the if block below.
user_choice = input('Do you want rock,paper or scissors?')
print('Computer Choice:', computer_choice)

###user_choice = input("What is your choice? ")
if computer_choice == 'paper' and user_choice == 'scissors':
    print('You won the game')
elif computer_choice == 'scissors' and user_choice == 'paper':
    print('You won the game')
elif computer_choice == 'paper' and user_choice == 'rock':
    print('You won the game')
elif computer_choice == 'rock' and user_choice == 'paper':
    print('You won the game')
else:
    print('All your choices are wrong ... BYE BYE')
    