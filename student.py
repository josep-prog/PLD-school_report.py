#!/bin/bash

# student.py
class Student:
    def __init__(self, name, gender, grades):
        self.name = name
        self.gender = gender
        self.grades = grades

    def calculate_average(self):
        """Calculate the average grade of the student"""
        return sum(self.grades) / len(self.grades)

    def promotion_status(self):
        """Determine if the student is promoted or projected to repeat the module"""
        average = self.calculate_average()
        if average >= 90:
            return "Recommended for extra weekend activities."
        elif average >= 50:
            return "Promoted to the next level."
        else:
            return "Projected to repeat the module."

    def get_report(self):
        """Return the formatted report for the student"""
        report = f"Name: {self.name}\nGender: {self.gender}\nGrades: {self.grades}\n"
        report += f"Average: {self.calculate_average():.2f}\n"
        report += f"Status: {self.promotion_status()}\n"
        return report
