# importing excell file in python and performing basic operations
# used pandas to import the excell file
import pandas as pd

# the excell file is stored in this variable
file = pd.read_excel('emp.xlsx', header=0)
emp_id = input('Enter Employee ID')
for i in file['Emp.ID']:
    if i == emp_id:
        # this code gets the salary of the specified employee
        sal = file.loc[file['Emp.ID'] == emp_id, 'salary']
        print(sal)
    else:
        print('Enter a valid Employee Id')
        break
