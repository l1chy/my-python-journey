name = input("Enter your full name: ").strip().title()
birth_date = input("Enter your birthdate (dd-mm-yyyy): ")
current_year = input("Enter the current year: ")
age = int(current_year) - int(birth_date.split("-")[2])
first_name = name.split()[0]

print('-'*25)
print(f"Hello, {first_name}\nWelcome at the age calculator!")
print('-'*25)
print(f"Your age is: {age}")