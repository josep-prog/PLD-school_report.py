class Student:
    def __init__(self, name, gender, grades):
        self.name = name
        self.gender = gender
        self.grades = grades
    
    def calculate_average(self):
        # Calculate the average of the grades
        return sum(self.grades) / len(self.grades)
    
    def determine_promotion(self):
        average = self.calculate_average()
        if average >= 90:
            return "Recommended for real-life application module"
        elif average >= 50:
            return "Promoted to the next level"
        else:
            return "Projected to repeat the module"
    
    def generate_report(self):
        # Generate a formatted report for the student
        average = self.calculate_average()
        promotion_status = self.determine_promotion()
        
        report = (
            f"Name: {self.name}\n"
            f"Gender: {self.gender}\n"
            f"Grades: {', '.join(map(str, self.grades))}\n"
            f"Average Grade: {average:.2f}\n"
            f"Promotion Status: {promotion_status}\n"
        )
        
        return report
