from flat import Bill, Flatmate
from reports import PdfReport

amount = float(input('Enter the bill amount: '))
period = input('What is the bill period? E.g. June 2023: ')

bill = Bill(amount=amount, period=period)


name1 = input(f'What is your name? ')
day_stay1 = int(input(f'How many days did {name1} stay in the house during the bill period? '))

name2 = input(f'What is your name? ')
day_stay2 = int(input(f'How many days did {name2} stay in the house during the bill period? '))

flatmate1 = Flatmate(name=name1, days_in_house=day_stay1)
flatmate2 = Flatmate(name=name2, days_in_house=day_stay2)

pdf_report = PdfReport(filename=f"{bill.period}.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=bill)
