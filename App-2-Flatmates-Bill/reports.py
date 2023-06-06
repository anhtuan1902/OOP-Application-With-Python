import webbrowser
import os
from fpdf import FPDF


class PdfReport:
    """
    Create a PDF file that contains data about the flatmates such as their name, their due amount,
     and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image("files/house.png", w=30, h=30)

        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', align='C', ln=1)
        pdf.set_font(family='Times', size=16, style='B')
        pdf.cell(w=100, h=25, txt='Period:')
        pdf.cell(w=150, h=25, txt=bill.period, ln=1)

        pdf.set_font(family='Times', size=14)
        pdf.cell(w=100, h=25, txt=f'{flatmate1.name}: {flatmate1.pay(bill=bill, flatmate2=flatmate2)}', ln=1)
        pdf.cell(w=100, h=25, txt=f'{flatmate2.name}: {flatmate2.pay(bill=bill, flatmate2=flatmate1)}', ln=1)

        os.chdir('files')
        pdf.output(self.filename)

        webbrowser.open(self.filename)
