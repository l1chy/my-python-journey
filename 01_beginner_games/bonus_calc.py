juniors = ['1111', '1113', '1115', '1117',
'1119', '1121']
mid_level = ['1311', '1313', '1315', '1317',
'1319', '1321', '1323', '1325']
seniors = ['1519', '1521', '1523', '1525']

id = input("Enter employee ID: ")
rate = float(input("Enter hourly rate: "))
hours = float(input("Enter hours worked this month: "))
salary = rate * hours
print('-'*35)

if id in juniors:
  bonus = salary * 3
elif id in mid_level:
  bonus = salary * 6
elif id in seniors:
  bonus = salary * 9
else:
  bonus = None
  print("Not an employee.")

if bonus != None:
  print(f'{id} gets a bonus of {bonus} EGP')