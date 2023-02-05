import tkinter as tk
from tkinter import filedialog
from script import generate_certificates
from tkinter import ttk

class CertificateGeneratorGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title("Certificate Generator GUI")
        self.geometry("400x300")
        
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
 
    def select_csv(self):
        file_path = filedialog.askopenfilename()
        
        subject = self.subject_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        webinar = self.webinar_entry.get()
        date = self.date_entry.get()
        generate_certificates(
            file_path=file_path,
            subject=subject, 
            user_email=email, 
            password=password,
            webinar=webinar,
            date=date
        )


app = CertificateGeneratorGUI()
app.mainloop()
