import tkinter as tk
from tkinter import filedialog
from script import generate_certificates

class CertificateGeneratorGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title("Certificate Generator GUI")
        self.geometry("400x200")
        
        label = tk.Label(self, text="Welcome to the Certificate Generator GUI!", font=("TkDefaultFont", 14))
        label.pack(pady=20)
        
        button = tk.Button(self, text="Select CSV File", command=self.select_csv)
        button.pack()
        
    def select_csv(self):
        file_path = filedialog.askopenfilename()
        generate_certificates(file_path)

app = CertificateGeneratorGUI()
app.mainloop()
