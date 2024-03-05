import csv
import openpyxl


with open('data.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    data = list(reader)


wb = openpyxl.Workbook()
sheet = wb.active


for row_index, row in enumerate(data, start=1):
    for column_index, value in enumerate(row, start=1):
        sheet.cell(row=row_index, column=column_index, value=value)


wb.save('task.xlsx')
