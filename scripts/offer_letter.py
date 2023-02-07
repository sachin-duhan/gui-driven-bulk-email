#! /usr/bin/python3

__author__ = "Sachin duhan"
__version__ = "0.0.1"

from docx import Document

def generate_document(template_file: str, output_file: str, values: dict):
    """generates offer letter document.

    Args:
        template_file (docx file): template offer letter with variable
        output_file: generated output file.
        values: dict of values to be changed.
    """
    document = Document(template_file)
    for paragraph in document.paragraphs:
        for key, value in values.items():
            if key in paragraph.text:
                paragraph.text = paragraph.text.replace("$" + key, value)
    document.save(output_file)
