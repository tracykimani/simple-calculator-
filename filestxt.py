import pandas as pd
from pandas import ExcelFile

file: ExcelFile = pd.ExcelFile('\Users\xlil-\OneDrive\Desktop/original.xlsx')
print(file.sheet_names)
