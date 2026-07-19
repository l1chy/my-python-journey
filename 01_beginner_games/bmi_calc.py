height = float(input("Enther height in cm: "))
weight = float(input("Enter weight in kg: "))
bmi = weight / ((height/100)**2)

if bmi < 18.5:
  body_type = "Underweight"
elif bmi <= 25:
  body_type = "Healthy"
elif bmi <= 30:
  body_type = "Overweight"
else:
  body_type = "Obese"

print('-'*20)
print(f"Your BMI is {bmi:.2f} and is considered {body_type}")
