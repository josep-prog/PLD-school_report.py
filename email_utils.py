import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, parent_name, parent_email, student_name, status, position_status, avg):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Standard port for sending email

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

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = parent_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, parent_email, msg.as_string())
        server.quit()
        print(f"Email sent to {parent_email} for {student_name}.")
    except Exception as e:
        print(f"Failed to send email to {parent_email} for {student_name}: {e}")
