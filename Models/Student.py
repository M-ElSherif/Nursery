import sys


class Student:

    def __init__(self, name, age=0, grade=0):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return self.name