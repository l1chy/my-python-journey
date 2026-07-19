print(f"Please enter scores between 0 ~ 100\n{'-'*35}")
ar = float(input("Enter Arabic score: "))
eng = float(input("Enter English score: "))
math = float(input("Enter Maths score: "))
bio = float(input("Enter Biology score: "))
chem = float(input("Enter Chemistry score: "))
phy = float(input("Enter Physics score: "))
percentage = ((ar+eng+math+bio+chem+phy)/600) * 100
score = (ar+eng+math+bio+chem+phy)/6
print('-'*35)

if not (0 <= score <= 100):
  grade = None
  print("Please enter valid numbers between 0 ~ 100")
elif percentage >= 90:
  grade = "A"
elif percentage >= 80:
  grade = "B"
elif percentage >= 70:
  grade = "C"
elif percentage >= 60:
  grade = "D"
else:
  grade = "F"

if grade != None:
  print(f"Your score is {percentage:.2f}%\nYour grade is {grade}")

