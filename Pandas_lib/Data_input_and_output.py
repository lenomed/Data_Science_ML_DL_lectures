import pandas as pd

pd.read_csv('example')
df = pd.read_csv('example')
#print(df)
write_to_csv = df.to_csv("new_csv", index=False)
print(write_to_csv)
print(pd.read_csv('new_csv'))
print("_"*50)

import pandas as pd

# 1. Read the original Excel file
df2 = pd.read_excel('Excel_Sample.xlsx', sheet_name='Sheet1')

print("Original DataFrame:")
print(df2)
print("_" * 50)

# 2. Write to new Excel file (correct way)
df2.to_excel('new_excel.xlsx',
             sheet_name='sheet1',   # Use consistent sheet name
             index=False)

print("Data successfully written to 'new_excel.xlsx' (sheet: new_sheet)")
print("_" * 50)

# 3. Read back from the new file (use the correct sheet name)
readx = pd.read_excel('new_excel.xlsx', sheet_name='sheet1')

print("Data read back from new file:")
print(readx)
print("_" * 50)

# Optional: Check if they are the same
print("Are both DataFrames equal?", df2.equals(readx))