#!/usr/bin/env python3

# student_report.py

from email_utils import send_email
from student import Student
from tabulate import tabulate
import time

# List of students and their grades
students_data = [
    ("BIZIYAREMYE Fabien", "Male", [98, 55, 60, 78]),
    ("NYIRAMANA Astherie", "Female", [43, 70, 73, 69]),
    ("HABANABASHAKA Jean Claude", "Male", [70, 90, 70, 87]),
    # Add more students as necessary...
]

# Function to send student reports
def send_student_reports():
    for idx, student in enumerate(students_sorted):
        avg = student.calculate_average()
        status = "Promoted" if avg >= 50 else "Repeat"
        position_status = f"Position: {idx+1} in class"

        parent_name, parent_email = get_parent_email(student.name)

        # Send the email based on student performance
        if avg >= 90:
            send_email(sender_email, sender_password, parent_name, parent_email, student.name, "Outstanding Academic Achievement", position_status, avg)
        elif avg < 50:
            send_email(sender_email, sender_password, parent_name, parent_email, student.name, "Needs Improvement", position_status, avg)
        else:
            send_email(sender_email, sender_password, parent_name, parent_email, student.name, "Average Performance", position_status, avg)

        # Print the report using tabulate
        headers = ["Name", "Gender", "Physics", "Chemistry", "Biology", "English", "Average", "Status", "Position Status"]
        row = [
            student.name,
            student.gender,
            *student.grades,
            avg,
            status,
            position_status
        ]

        print(f"Student Report for {student.name}")
        print(tabulate([row], headers=headers, tablefmt="fancy_grid"))
        print("\n" + "="*50 + "\n")

        time.sleep(1)  # Delay between emails

# Your main logic or execution code
if __name__ == "__main__":
    send_student_reports()
