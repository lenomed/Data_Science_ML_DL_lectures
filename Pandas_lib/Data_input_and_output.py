import pandas as pd

pd.read_csv('example')
df = pd.read_csv('example')
#print(df)
write_to_csv = df.to_csv("new_csv", index=False)
print(write_to_csv)
print(pd.read_csv('new_csv'))
print("_"*50)

pd.read_excel('Excel_Sample.xlsx',sheetname='Sheet1')
write_to_x = df.to_excel('Excel_Sample.xlsx',sheet_name='Sheet1')
print(write_to_x)


df3 = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
print(df3[0])