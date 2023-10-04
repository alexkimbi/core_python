#!/usr/bin/python3
computer_choice = input("What is the computer's choice? ")
user_choice = input("What is your choice? ")
if computer_choice == 'paper' and user_choice == 'scissors':
    print('You won the game')
elif computer_choice == 'scissors' and user_choice == 'paper':
    print('You won the game')
elif computer_choice == 'paper' and user_choice == 'rock':
    print('You won the game')
elif computer_choice == 'rock' and user_choice == 'paper':
    print('You won the game')
else:
    print('All your choices arewrong ... BYE BYE')