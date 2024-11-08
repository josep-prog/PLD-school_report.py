#!/usr/bin/env python3

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to send emails using smtplib
def send_email(sender_email, sender_password, parent_name, parent_email, student_name, status, position_status, avg, message):
    # SMTP server configuration
    smtp_server = "smtp.gmail.com"  # Use Gmail as an example
    smtp_port = 587  # Standard port for sending email

    # Create the email content
    subject = f"{status} Report for {student_name}"
    body = f"""
    {subject}

    Dear {parent_name},

    I hope you are doing well. I am happy to share that your child, {student_name}, has done an amazing job in their studies, scoring an average of {avg:.2f}. Based on this result, we would like to inform you of the following:

    {message}

    Meeting Details:
        - Date: 17th December 2024
        - Time: 9:00 AM to 11:00 AM
        - Location: BlueLakes International School Main Hall

    Please let us know if you can attend the meeting. If you have any questions before then, feel free to contact me.

    Best regards,   
    Group9_PLD-project
    Student Software Department
    African Leadership University
    0791646062
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
    except smtplib.SMTPAuthenticationError as e:
        print(f"Authentication failed for {parent_email}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
