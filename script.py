#! /usr/bin/python3 

__author__ = "Sachin duhan"

import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from config import settings

def generate_certificates(file_path: str, subject: str, user_email: str = None, password: str = None):
    if user_email is None:
        user_email = settings.SMTP_USERNAME
    if password is None:
        password = settings.SMTP_PASSWORD

    # Read the CSV file
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        next(reader) # skip the header row
        for row in reader:
            name = row[0]
            email = row[1]

            # Generate a certificate for each candidate
            with open("certificate.txt", "w") as certificate:
                certificate.write(f"Certificate of Completion\n\n")
                certificate.write(f"This is to certify that {name} has completed the webinar\n")
                certificate.write(f"Date: [Insert Date Here]\n\n")
                certificate.write("Signed,\n[Your Signature]")

            # Send an email with the certificate
            msg = MIMEMultipart()
            msg['Subject'] = subject
            msg['From'] = user_email
            msg['To'] = email

            with open("certificate.txt", "r") as f:
                certificate_text = MIMEText(f.read(), 'plain')
                msg.attach(certificate_text)

            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(user_email, password)
            s.sendmail(user_email, email, msg.as_string())
            s.quit()


print(settings.SMTP_SERVER)