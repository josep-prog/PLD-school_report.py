#!/usr/bin/env python3


class Student:
    def __init__(self, name, gender, grades):
        self.name = name
        self.gender = gender
        self.grades = grades

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)
