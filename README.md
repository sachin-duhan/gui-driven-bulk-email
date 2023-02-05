# Certificate Generator

This is a simple Python script that generates certificates and sends them via email to candidates based on their name and email address, which are stored in a CSV file. The script includes a Tkinter GUI that allows users to select the CSV file and run the script.

## Features

Reads candidate information from a CSV file
Generates a certificate in text format for each candidate
Sends the certificate via email to each candidate
Includes a Tkinter GUI for user-friendly interaction
Uses environment variables or Dynaconf for storing sensitive information
Requirements

- Python 3
- Tkinter library for GUI
- smtplib library for sending emails
- csv library for reading CSV files
- email library for constructing email messages
- Dynaconf (optional) for storing sensitive information


## Installation

- Clone the repository: git clone [here](https://github.com/sachin-duhan26/gui-driven-bulk-email.git)
```bash
pip install --upgrade pip
pip --version
pip3 install virtualenv
source .venv/bin/activate
make install
```
- Update the configuration file with your environment variables ```settings.toml```


## Usage

- Create a CSV file with candidate names and email addresses
Run the project: ```make run```
- Use the Tkinter GUI to select the CSV file and run the script
Limitations

Currently, the script only supports sending emails via Gmail.
The certificate format is fixed and cannot be customized.
The date on the certificate is not automatically inserted and must be manually updated.

## Contributions

Contributions are welcome! If you would like to contribute to this project, please create a fork, make your changes, and submit a pull request.