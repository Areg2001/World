from myObjects import Grass, Sun, Frog, Tree
# import time, os

limit = int(input("Enter limit of frogs eating with count."))
hours = int(input("How many hours is your day have?"))
hours = 3600 * hours
start = 0


class World:

    def __init__(self):
        self.sun = Sun()
        self.grass = Grass()
        self.frog = Frog(limit)
        self.tree = Tree()

    @staticmethod
    def isLight():
        if start < (hours / 2):
            return "The sun is shining."

        return "The sun is not shining."

    @staticmethod
    def haveAir():
        if start < (hours / 2):
            return "The tree produces oxygen."

        return "The tree not produces oxygen"

    @staticmethod
    def frogIsEating():
        if start < (hours / 2) and (start <= limit):
            return "Frog is eating."

        return "Frog is not eating."

    @staticmethod
    def frogIsAwake():
        if start < (hours / 2):
            return "Frog is awake."

        return "Frog is sleeping."

    def __str__(self):
        return f"{self.isLight(), self.haveAir(), self.frogIsEating(), self.frogIsAwake()}"


world = World()




