#!/usr/bin/env python3
import os
from student import Student

# A list of student data: (Name, Gender, Grades)
student_data = [
    ("Alice", "Female", [85, 92, 78, 88]),
    ("Bob", "Male", [50, 55, 48, 60]),
    ("Charlie", "Male", [95, 90, 93, 91]),
    ("Diana", "Female", [45, 48, 42, 40]),
    # Add more student data as needed
]

def generate_student_report():
    # Create student objects and generate reports
    students = []
    for data in student_data:
        student = Student(name=data[0], gender=data[1], grades=data[2])
        students.append(student)
    
    # Sort students by average grade (in descending order)
    students_sorted = sorted(students, key=lambda x: x.calculate_average(), reverse=True)
    
    # Display each student's report
    for index, student in enumerate(students_sorted, start=1):
        report = student.generate_report()
        print(f"\n--- Report for {student.name} (Rank: {index}) ---")
        print(report)

if __name__ == "__main__":
    generate_student_report()
