#! /usr/bin/python3 

__author__ = "Sachin duhan"

import os
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from config import settings
from datetime import date
from PIL import Image, ImageDraw, ImageFont

FONT_SIZE = 100

def getNameXCord(name):
    OFFSET_FACTOR = 35
    BASE_X_VAL = 1000
    name = str(name)
    retVal = BASE_X_VAL - (OFFSET_FACTOR * len(name)-1)
    return retVal

def removeTempororyFiles(path: str = 'tmp') -> None:
    """remove all files in a given folder path

    Args:
        path (str): folder path; DEFAULT = 'tmp'
    """
    for f in os.listdir(path):
        if f.endswith(".md"):
            continue
        os.remove(os.path.join(path, f))

def generate_certificates(
        file_path: str, 
        subject: str, 
        user_email: str = None, 
        password: str = None, 
        webinar: str = "Placement preparation workshop", 
        _date: str = date.today()
    ):

    """Certificate generator function that creates and send email attachment of the created certificate.

    Args:
        file_path (str): CSV file path with names and emails.
        subject (str): subject of the email to be sent to user.
        user_email (str, optional): user email for smtp server. Defaults to None.
        password (str, optional): password for smtp server. Defaults to None.
        webinar (str, optional): webinar name that can be added to certificate. Defaults to None.
        date (str, optional): webinar conduct date. Defaults to None.
    """

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

            with Image.open("utils/certificate_template.png").convert("RGBA")  as base:
                txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
                nameFnt = ImageFont.truetype("fonts/TIMES.ttf", FONT_SIZE)
                webinarFnt = ImageFont.truetype("fonts/TIMES.ttf", 40)
                d = ImageDraw.Draw(txt)
                d.text((getNameXCord(name), 600), name.upper(), font=nameFnt, fill=(0, 0, 0, 255))
                d.text((820, 850), webinar, font=webinarFnt, fill=(0, 0, 0, 255))
                d.text((600, 910), _date.upper(), font=webinarFnt, fill=(0, 0, 0, 255))
                out = Image.alpha_composite(base, txt)
                out.save("tmp/certificate.png")

            with open('certificate.png', 'rb') as f:
                img_data = f.read()

            # Send an email with the certificate
            msg = MIMEMultipart()
            msg['Subject'] = subject
            msg['From'] = user_email
            msg['To'] = email

            image = MIMEImage(img_data, name=os.path.basename('certificate.png'))
            msg.attach(image)

            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(user_email, password)
            s.sendmail(user_email, email, msg.as_string())
            s.quit()
        
    removeTempororyFiles()

