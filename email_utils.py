import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from student import Student
from tabulate import tabulate

# List of students and their grades
students_data = [
    ("BIZIYAREMYE Fabien", "Male", [98, 55, 60, 78]),
    ("NYIRAMANA Astherie", "Female", [43, 70, 73, 69]),
    ("HABANABASHAKA Jean Claude", "Male", [70, 90, 70, 87]),
    # Add more students as necessary...
]

# Get parent details
def get_parent_email(student_name):
    parents = {
        "NKURUNZIZA Isabelle": ("Joseph Nishimwe", "nishimwejoseph26@gmail.com"),
        "NYIRANDIKUMANA Sophie": ("Joseph Nishimwe", "josephnishimwe398@gmail.com"),
        "UWUMUKIZA Jeannine": ("David Kayumba", "d.kayumba1@alustudent.com"),
        "MUREBWAYIRE Samuel": ("Amanda Inema", "a.inema2@alustudent.com"),
        "NDAGIJIMANA Kabuye": ("Joseph Nishimwe", "nishimwejoseph26@gmail.com"),
    }
    
    if student_name not in parents:
        return ("Nishimwe Joe", "j.nishimwe@alustudent.com")
    
    return parents[student_name]

# Create Student objects
students = [Student(name, gender, grades) for name, gender, grades in students_data]

# Sort students by average score in descending order
students_sorted = sorted(students, key=lambda student: student.calculate_average(), reverse=True)

# Function to send emails using smtplib (corrected with 8 parameters)
def send_email(sender_email, sender_password, parent_name, parent_email, student_name, status, position_status, avg):
    # SMTP server configuration
    smtp_server = "smtp.gmail.com"  # Use Gmail as an example
    smtp_port = 587  # Standard port for sending email

    # Create the email content
    subject = f"{status} Report for {student_name}"
    body = f"""
    Subject: {status} Report for {student_name}

    Dear {parent_name},

    I hope this message finds you well.

    I am writing to inform you of the academic performance of your child, {student_name}.
    Their recent performance has been evaluated, and they have achieved an average score of {avg:.2f}. Based on this result:

    Status: {status}
    Position: {position_status}

    If you have any questions or need further information, please feel free to reach out.

    Best regards,
    [Your Full Name]
    [Your Position]
    BlueLakes International School (BLIS)
    [Contact Information]
    """

    # Set up the MIME structure for the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = parent_email
    msg['Subject'] = subject

    # Attach the body content to the email
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Use TLS encryption for security
        server.login(sender_email, sender_password)  # Log in to the SMTP server
        text = msg.as_string()
        server.sendmail(sender_email, parent_email, text)  # Send the email
        server.quit()  # Quit the server after sending the email
        print(f"Email sent to {parent_email} for {student_name}.")
    except Exception as e:
        print(f"Failed to send email to {parent_email} for {student_name}: {e}")

# Function to send emails based on conditions
def send_student_reports():
    for idx, student in enumerate(students_sorted):
        avg = student.calculate_average()
        status = "Promoted" if avg >= 50 else "Repeat"
        position_status = f"Position: {idx+1} in class"
        
        # Email details
        parent_name, parent_email = get_parent_email(student.name)
        
        # Send emails based on performance levels
        if avg >= 90:
            send_email(sender_email, sender_password, parent_name, parent_email, student.name, "Outstanding Academic Achievement", position_status, avg)
        elif avg < 50:
            send_email(sender_email, sender_password, parent_name, parent_email, student.name, "Needs Improvement", position_status, avg)
        else:
            send_email(sender_email, sender_password, parent_name, parent_email, student.name, "Average Performance", position_status, avg)
        
        # Print the individual report using tabulate
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
        print("\n" + "="*50 + "\n")  # Separator between reports

# SMTP configuration details (replace with your actual values)
sender_email = "j.nishimwe@alustudent.com"  # Your email address
sender_password = "pkykztfwroaygsf"  # Your email password or app-specific password

# Start sending student reports
send_student_reports()
