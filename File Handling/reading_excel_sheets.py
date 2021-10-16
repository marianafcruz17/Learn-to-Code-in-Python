import pandas as pd

file = pd.ExcelFile("/Users/Maria/Desktop/sales.xlsx")
print(file.sheet_names)

sheets = file.parse('sales')
print(sheets)
