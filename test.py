#!/usr/bin/python3
username = input("What is your name?")
print(username)
if username == 'Alex Song':
    print ("You got the right name")
else:
    print("Get out of my system.")
index = username.index(username)
print('The index of index:', index)
