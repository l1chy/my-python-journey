from datetime import datetime

dob = int(input("Whats the year you were born?: ")) # Date of Birth
current_year = datetime.now().year
age = current_year - dob

print(f"You're {age} years old.")