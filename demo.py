import pandas as pd

file = pd.read_excel('emp.xlsx', header=0)
emp_id = input('Enter Employee ID')
id_in_file = file.loc[file['Emp_ID'] == emp_id]
print(id_in_file)
