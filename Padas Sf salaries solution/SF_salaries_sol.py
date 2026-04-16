import pandas as pd

sal = pd.read_csv('Salaries.csv')
data_header = sal.head()
print(data_header)
print('_'*50)
infomation = sal.info()
print(infomation)
print('_'*50)
base_pay = sal['BasePay'] = pd.to_numeric(sal['BasePay'], errors='coerce')
print(base_pay.mean())
over_time_pay = sal['OvertimePay'] = pd.to_numeric(sal['OvertimePay'], errors='coerce')
print("_"*50)
print(f"over time pay: {over_time_pay.max()}")

employee_job_title = sal[sal['EmployeeName']== "JOSEPH DRISCOLL"]
print(employee_job_title.TotalPay)
print("_"*50)

highest_paid =sal[sal['TotalPay'] == sal['TotalPay'].max()]
highest_paid2 = sal.iloc[[sal['TotalPay'].idxmax()]]
lowest_paid = sal.iloc[[sal['TotalPay'].idxmin()]]
print(f'lowest paid: {lowest_paid}')
print(highest_paid)
print(highest_paid2)

print('_'*50)
year = sal.groupby("Year").mean(numeric_only=True)
print(year)

job_titles = len(sal['JobTitle'].unique())# you can also use the nunique() method instead of len() method
print(job_titles)
top_five = sal['JobTitle'].value_counts().head(5)
print("_"*50)

print(f"Top five job titles are: {top_five}")
job1 = sum(sal[sal["Year"]==2013]['JobTitle'].value_counts()==1)
print(f"job that was represented by only one person {job1}")

print("_"*50)

def get_cheif(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False
get_cheif('chief')
print('_'*50)
chief_string = sal['JobTitle'].apply(lambda x: get_cheif(x))
print(f'number of chieves are: {len(chief_string)}')

sal['title_len'] = sal['JobTitle'].apply(len)
listed = sal[["TotalPay","title_len"]].corr()
print(listed)





