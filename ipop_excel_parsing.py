from ctypes import sizeof
import pandas as pd
import os

#path of the directory in which excel file is present
data_folder = os.path.dirname(os.path.abspath(__file__))
#name of the excel file with extension
excel_filename = "ipop_excel.ods"    
#open workbook   
workbook = pd.read_excel(os.path.join(data_folder, excel_filename), sheet_name="Sheet1")

#Gives number of rows
count_row = workbook.shape[0]
#Gives number of columns
count_col = workbook.shape[1]

#row index starts from 0
row_idx = 0
#go through all the rows
for row_idx in range(count_row):
    print(workbook.iloc[row_idx, 0], workbook.iloc[row_idx, 1])
