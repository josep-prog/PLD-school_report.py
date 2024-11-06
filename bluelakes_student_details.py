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
    
    # More students added with varied and unrelated marks
    ("KAGABO Donatien", "Male", [65, 45, 50, 68]),
    ("MURORANKWAVU Alice", "Female", [90, 88, 92, 85]),
    ("SABINIMANA Jean Pierre", "Male", [50, 60, 55, 70]),
    ("NYIRANDIKUMANA Chantal", "Female", [85, 90, 75, 80]),
    ("RUTAGENGWA Edmond", "Male", [72, 65, 58, 88]),
    ("UWUMUKIZA Jeannine", "Female", [94, 92, 91, 89]),
    ("MUKAMANA Valentine", "Female", [66, 78, 70, 72]),
    ("KABANDA Olivier", "Male", [80, 85, 88, 91]),
    ("NGABO Celestin", "Male", [47, 62, 55, 60]),
    ("HABUMUGISHA Simeon", "Male", [70, 75, 68, 80]),
    ("TUYISHIMIRE Emmanuellie", "Male", [56, 59, 50, 67]),
    ("NKURUNZIZA Isabelle", "Female", [98, 97, 93, 94]),
    ("NDAGIJIMANA Kabuye", "Male", [45, 39, 50, 60]),
    ("MAKARA Gisele", "Female", [72, 78, 66, 74]),
    ("HABUMUGISHA Leonce", "Male", [80, 85, 75, 77]),
    ("NDIKUMANA Adeline", "Female", [60, 70, 80, 65]),
    ("RUKUNDO Innocent", "Male", [88, 85, 90, 92]),
    ("UMUGENZI Solange", "Female", [72, 80, 69, 60]),
    ("MUGISHA Paul", "Male", [60, 62, 55, 50]),
    ("RUBANGURA Aimable", "Male", [55, 66, 62, 59]),
    ("MUREBWAYIRE Samuel", "Male", [90, 91, 89, 94]),
    ("IRAGUHA Rose", "Female", [50, 60, 55, 52]),
    ("NZAMURINSHI Janet", "Female", [84, 79, 82, 85]),
    ("KAMARA Alain", "Male", [60, 68, 75, 72]),
    ("NYIRANDIKUMANA Sophie", "Female", [93, 94, 88, 97]),
    ("MUKANDAYISABYE Olive", "Female", [77, 81, 90, 75]),
    ("MULINDWA Evariste", "Male", [76, 69, 80, 72]),
    ("HABIMANA Hope", "Male", [90, 85, 89, 88]),
    ("MURWIRAMBA Divine", "Female", [72, 80, 85, 90]),
    ("KABANDA Jospin", "Male", [62, 60, 50, 55]),
    ("NAHIMANA Trésor", "Male", [88, 91, 80, 92]),
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
