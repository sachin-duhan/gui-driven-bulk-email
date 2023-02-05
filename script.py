#! /usr/bin/python3 

__author__ = "Sachin duhan"

import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from config import settings
from PIL import Image, ImageDraw, ImageFont
import os.path

FONT_SIZE = 100

def getNameXCord(name):
    OFFSET_FACTOR = 35
    BASE_X_VAL = 1000
    name = str(name)
    retVal = BASE_X_VAL - (OFFSET_FACTOR * len(name)-1)
    return retVal


def generate_certificates(file_path: str, subject: str, user_email: str = None, password: str = None, webinar: str = None, date: str = None):
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

            with Image.open("./cert.png").convert("RGBA")  as base:
                txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
                # get a font
                nameFnt = ImageFont.truetype("TIMES.ttf", FONT_SIZE)
                webinarFnt = ImageFont.truetype("TIMES.ttf", 40)
                # get a drawing context
                d = ImageDraw.Draw(txt)

                # draw text
                d.text((getNameXCord(name), 600), name.upper(), font=nameFnt, fill=(0, 0, 0, 255))
                d.text((820, 850), webinar, font=webinarFnt, fill=(0, 0, 0, 255))
                d.text((600, 910), date.upper(), font=webinarFnt, fill=(0, 0, 0, 255))

                out = Image.alpha_composite(base, txt)
                out.save("certificate.png")

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


print(settings.SMTP_SERVER)