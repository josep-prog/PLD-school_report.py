#!/usr/bin/env python3
# bluelakes_student_details.py

from student import Student

# List of students and their grades
students_data = [
    # Name, Gender, Grades in [Physics, Chemistry, Biology, English]
    ("BIZIYAREMYE Fabien", "Male", [98, 55, 60, 78]),
    ("NYIRAMANA Astherie", "Female", [43, 70, 73, 69]),
    ("HABANABASHAKA Jean Claude", "Male", [70, 90, 70, 87]),
    ("MUKAYISENGA Deborah", "Female", [67, 90, 50, 64]),
    ("UWIRINGIYIMANA Esther", "Female", [77, 80, 70, 81]),
    ("IZABAYO Bernardine", "Female", [78, 80, 90, 58]),
    ("NIYONAGIRA Lilianne", "Female", [98, 86, 50, 78]),
    ("Joeyeux Munezero", "Female", [78, 80, 98, 98]),
    ("KUBWUMUREMYI Jeanne Alice", "Female", [78, 80, 90, 98]),
    ("DUFITIMANA Frida", "Female", [78, 80, 90, 98]),
    ("Thomas HABANABAKIZE", "Male", [78, 80, 90, 98]),
    ("UZAYISABA Mathilde", "Female", [78, 80, 90, 98]),
    ("NIYONZIZA Rahab", "Female", [78, 80, 90, 98]),
    ("TURIKUMWENAYO Theodette", "Female", [78, 80, 90, 98]),
    ("MURWANASHYAKA Emmanuel", "Male", [78, 80, 90, 98]),
    ("Marie Josee MUKATUYISENGE", "Female", [78, 80, 90, 98]),
    ("NYIRAZANINKA Micheline", "Female", [78, 80, 90, 98]),
    ("TWAGIRAYEZU Jean Marie Vianney", "Female", [78, 80, 90, 98]),
    # Add other students similarly...
]

# Create Student objects from the students_data list
students = [Student(name, gender, grades) for name, gender, grades in students_data]

# Sort students by average score in descending order
students_sorted = sorted(students, key=lambda student: student.calculate_average(), reverse=True)

# Output the sorted report
for rank, student in enumerate(students_sorted, start=1):
    print(f"Rank {rank}:")
    print(student.get_report())
    print("=" * 50)  # Separator between reports
