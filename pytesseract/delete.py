import os
from pprint import pprint
import openpyxl

cwd = os.getcwd()

dirs = [
    os.path.join(cwd, 'output-txt'), 
    os.path.join(cwd, 'img_heic'), 
    os.path.join(cwd, 'img_cropped'),
    os.path.join(cwd, 'img_boxed') 
        ]

for dir in dirs:
    print('> Scanning the folder: {dir_name}...'.format(dir_name=dir))
    files = [os.path.join(dir, item) for item in os.listdir(dir)]
    
    if len(files) >= 1:
        print('> Deleting the files from the folder ...')
        for file in files:
            os.remove(file)
        print('> Files in the folder removed')
    else: 
        print('> The folder is empty.')
        

# cleaning the data base file 
excel_file_path = os.path.join(cwd, 'output_data', 'customer_list-0.xlsx') 

print('=====================================')
wb = openpyxl.load_workbook(excel_file_path)
ws = wb['English']

rows = ws.max_row
print('=> deleting the data...')
ws.delete_rows(2, rows)
print('=> data deleted:', rows, 'rows')

wb.save(excel_file_path)