import os
from student import Student

class SchoolDatabase:
    def __init__(self):
        # A list of student data: (Name, Gender, Grades)
        self.student_data = [
            ("Alice", "Female", [85, 92, 78, 88]),
            ("Bob", "Male", [50, 55, 48, 60]),
            ("Charlie", "Male", [95, 90, 93, 91]),
            ("Diana", "Female", [45, 48, 42, 40]),
            ("BIZIYAREMYE Fabien", "Male", [98, 55, 60, 78]),
            ("NYIRAMANA Astherie", "Female", [43, 70, 73, 69]),
            ("HABANABASHAKA Jean Claude", "Male", [70, 90, 70, 87]),
            ("MUKAYISENGA Deborah", "Female", [67, 90, 50, 64]),
            ("UWIRINGIYIMANA Esther", "Female", [77, 80, 70, 81]),
            ("IZABAYO Bernardine", "Female", [78, 80, 90, 58]),
            ("NIYONAGIRA Lilianne", "Female", [98, 86, 50, 78]),
            ("Joeyeux Munezero", "Female", [78, 80, 98, 98]),
            ("KUBWUMUREMYI Jeanne Alice", "Female", [79, 81, 90, 98]),
            ("DUFITIMANA Frida", "Female", [80, 82, 90, 98]),
            ("Thomas HABANABAKIZE", "Male", [81, 83, 90, 98]),
            ("UZAYISABA Mathilde", "Female", [82, 84, 90, 98]),
            ("NIYONZIZA Rahab", "Female", [83, 85, 90, 98]),
            ("TURIKUMWENAYO Theodette", "Female", [84, 86, 90, 98]),
            ("MURWANASHYAKA Emmanuel", "Male", [85, 87, 90, 98]),
            ("Marie Josee MUKATUYISENGE", "Female", [86, 88, 90, 98]),
            ("NYIRAZANINKA Micheline", "Female", [87, 89, 90, 98]),
            ("TWAGIRAYEZU Jean Marie Vianney", "Female", [88, 90, 90, 98]),
            ("IBAHABONA Tharcisse", "Male", [89, 91, 90, 98]),
            ("UWUMUKIZA Adelina", "Female", [90, 92, 90, 98]),
            # Additional students can be added here...
        ]

    def calculate_average(self, grades):
        return sum(grades) / len(grades)

    def display_students(self):
        for name, gender, grades in self.student_data:
            average = self.calculate_average(grades)
            print(f"Name: {name}, Gender: {gender}, Average Grade: {average:.2f}")

# Example usage
if __name__ == "__main__":
    school_db = SchoolDatabase()
    school_db.display_students()
