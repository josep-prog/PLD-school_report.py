#!/usr/bin/env python3

from student import Student
from email_utils import send_email  # Importing the send_email function
from tabulate import tabulate

# List of students and their grades
students_data = [
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

# Example of the parent email retrieval function (adjust as needed)
def get_parent_email(student_name):
    parents = {
        "NKURUNZIZA Isabelle": ("Joseph Nishimwe", "nishimwejoseph26@gmail.com"),
        "NYIRANDIKUMANA Sophie": ("Joseph Nishimwe", "josephnishimwe398@gmail.com"),
        "NDAGIJIMANA Kabuye": ("David Kayumba", "d.kayumba1@alustudent.com"),
        "MUKAYISENGA Deborah": ("Amanda Inema", "a.inema2@alustudent.com"),
        "NYIRAMANA Astherie": ("Elisha Rurangwa", "e.rurangwa@alustudent.com"),
        # Add any other necessary students and their parent details
    }

    if student_name not in parents:
        # Return Joe Nishimwe as the default parent and his email
        return ("Joe Nishimwe", "josephnishimwe398@alustudent.com")
    
    return parents[student_name]

# Create Student objects
students = [Student(name, gender, grades) for name, gender, grades in students_data]

# Sort students by average score in descending order
students_sorted = sorted(students, key=lambda student: student.calculate_average(), reverse=True)

# Example: Your email credentials
sender_email = "j.nishimwe@alustudent.com"  # Your email address
sender_password = "notx xoli zbsl ywxq"  # Your app-specific password

# Send the emails and print the reports
for idx, student in enumerate(students_sorted):
    avg = student.calculate_average()
    status = "Promoted" if avg >= 50 else "Repeat"
    position_status = f"Position: {idx+1} in class"

    parent_name, parent_email = get_parent_email(student.name)

    # Construct the message based on the student's average score
    if avg >= 90:
        message = "Your child has achieved Outstanding Academic Achievement."
        send_email(sender_email, sender_password, parent_name, parent_email, student.name, status, position_status, avg, message)
    elif avg < 50:
        message = "Your child needs improvement and will need to repeat the class."
        send_email(sender_email, sender_password, parent_name, parent_email, student.name, status, position_status, avg, message)
    else:
        message = "Your child has an average performance. Please continue to encourage them."
        send_email(sender_email, sender_password, parent_name, parent_email, student.name, status, position_status, avg, message)
    
    # Print individual student report
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
