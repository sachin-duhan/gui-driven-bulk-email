#! python3.10

__author__ = "Sachin duhan"
__version__ = "0.1.1"

import tkinter as tk
from tkinter import filedialog
from scripts.certificate import generate_certificates
from tkinter import ttk
import csv

class CertificateGeneratorGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title("Certificate Generator GUI")
        self.geometry("400x500")
        
        label = ttk.Label(self, text="Welcome to the Certificate Generator GUI!", font=("TkDefaultFont", 14))
        label.pack(pady=20)
        
        # Email subject input
        subject_label = ttk.Label(self, text="Subject:")
        subject_label.pack()
        self.subject_entry = ttk.Entry(self)
        self.subject_entry.pack()
        
        # Email address input
        email_label = ttk.Label(self, text="Your email")
        email_label.pack()
        self.email_entry = ttk.Entry(self)
        self.email_entry.pack()
        
        # Email password input
        password_label = ttk.Label(self, text="Password")
        password_label.pack()
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack()

        # Webinar Subject Name
        webinar_label = ttk.Label(self, text="Webinar Name")
        webinar_label.pack()
        self.webinar_entry = ttk.Entry(self)
        self.webinar_entry.pack()
        
        # Email password input
        date_label = ttk.Label(self, text="Date")
        date_label.pack()
        self.date_entry = ttk.Entry(self)
        self.date_entry.pack()
        
        # CSV file selection button
        select_csv_button = ttk.Button(self, text="Select CSV File", command=self.select_csv)
        select_csv_button.pack()

        # Send email button
        send_email_button = ttk.Button(self, text="Send Emails", command=self.send_emails)
        send_email_button.pack()

         # Error label
        self.error_label = ttk.Label(self, text="", foreground="red")
        self.error_label.pack(pady=10)

                 # Error label
        self.success_label = ttk.Label(self, text="", foreground="green")
        self.success_label.pack(pady=10)
        
 
    def __validate_csv_file(self) -> bool:
        # Validate CSV file format and entries
        try:
            with open(self.csv_file) as csv_file:
                reader = csv.reader(csv_file)
                headers = next(reader)
                if headers != ["Name", "Email"]:
                    self.error_label.config(text="CSV file must have 'Name' and 'Email' headers.")
                    return False
                for row in reader:
                    name = row[0]
                    candidate_email = row[1]
                    if not name or not candidate_email:
                        self.error_label.config(text="CSV file must have values for both 'Name' and 'Email'.")
                        return False
            return True
        except Exception as e:
            self.error_label.config(text=f"Error reading CSV file: {e}")
            return False

    def send_emails(self):
        """driver function for validation and sending emails."""

        subject = self.subject_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        webinar = self.webinar_entry.get()
        date = self.date_entry.get()

        if not subject:
            self.error_label.config(text="Please enter a subject.")
            return
        if not email:
            self.error_label.config(text="Please enter an email address.")
            return
        if not password:
            self.error_label.config(text="Please enter a password.")
            return        
        if not webinar:
            self.error_label.config(text="Please enter a webinar name.")
            return
        if not date:
            self.error_label.config(text="Please enter a valid date.")
            return
        if not self.csv_file:
            self.error_label.config(text="Please select a CSV file.")

        generate_certificates(
            file_path=self.csv_file,
            subject=subject, 
            user_email=email, 
            password=password,
            webinar=webinar,
            date=date
        )
        self.success_label.config(text="Congratulations, Emailing started...")

    def select_csv(self):
        _file = filedialog.askopenfilename()
        if not self.__validate_csv_file():
            return
        self.csv_file = _file


app = CertificateGeneratorGUI()
app.mainloop()
