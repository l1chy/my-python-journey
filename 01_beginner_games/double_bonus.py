working_Hours = float(input("Enter the hours you worked per month: "))
hourly_Rate = float(input("Enter how much you get per hour: "))
base_hours = 100
salary = working_Hours * hourly_Rate
extra = (working_Hours - base_hours) * (hourly_Rate * 2)
print('-'*20)

if working_Hours > 100:
  salary = (base_hours * hourly_Rate) + extra
else:
  salary = working_Hours * hourly_Rate

print(f"You've worked {working_Hours} this month, your salary is {salary}")
  
  



