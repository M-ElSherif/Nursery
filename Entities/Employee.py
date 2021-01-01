import sys
from datetime import datetime, date


class Employee:

    def __init__(self, name: str, position: str, salary: float, join_date: str):
        self.name = name
        self.position = position
        self.salary = salary
        self.join_date = join_date

    def __repr__(self):
        return self.name
