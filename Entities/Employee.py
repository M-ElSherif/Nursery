import sys
from datetime import datetime


class Employee:

    def __init__(self, name: str, position: str, salary: float, join_date: datetime):
        self.name = name
        self.position = position
        self.salary = salary
        self.join_date = join_date

    def __repr__(self):
        return self.name
