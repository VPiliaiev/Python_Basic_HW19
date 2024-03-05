import openpyxl

wb = openpyxl.load_workbook('task.xlsx')

sheet = wb.active

sheet.delete_cols(3)

wb.save('task_delete_age.xlsx')
