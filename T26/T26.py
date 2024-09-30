import subprocess
import pandas as pd
import openpyxl as op

command = ["powershell.exe", "-File", "C:/T26/T26.ps1"]
subprocess.run(command, capture_output=True, text=True)

filecsv = pd.read_csv('C:\\T26\\services.csv')

filecsv.to_excel('services.xlsx', index=False)

b = op.load_workbook('services.xlsx')
h = b.active

for row in h.iter_rows(values_only=True):
    for cell in row:
        data = cell.split(',')       

b.save('C:\\T26\\services2.xlsx')
print('hola')
