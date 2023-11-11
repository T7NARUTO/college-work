import pandas as pd

file = pd.read_excel('emp.xlsx')
a = pd.read_excel('emp.xlsx', header=0)
emp = input('enter emp_id')
print(emp in a)
