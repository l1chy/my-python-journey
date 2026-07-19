fnum = int(input("First number: "))
snum = int(input("Second number: "))
process = input("What do you want to do? (+, -, *, /): ")

if process == "+":
  print("Result = ",fnum+snum)
elif process == "-":
  print("Result = ",fnum-snum)
elif process == "*":
  print("Result = ",fnum*snum)
elif process == "/":
  print("Result = ",fnum/snum)
else:
  print("Sorry I dont understand your input","("+process+")")