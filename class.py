#!/usr/bin/python3
class Robot:
    def __init__(self, n, c, w):
        self.name = n
        self.color = c
        self.weight = w
    def introduce_self(self):
        print("My name is " + self.name)
r1 = Robot("Tom", "red", "30")
r2 = Robot("Jerry", "blue", "40")

class person:
    def __init__(self, n, p, i):
        self.is_sitting = True
    def stand_up(self):
        self.is_sitting= False
P1 = person("Alice", "aggressive", False)
P2 = person("Bexky", "talk", True)