f_num = float(input("Enter first number: "))
s_num = float(input("Enter second number: "))
operator = input("Enter the operator: ")

if operator == "+":
  process = "Addition"
  result = f_num + s_num
elif operator == "-":
  process = "Substraction"
  result = f_num - s_num
elif operator == "*":
  process = "Multiplication"
  result = f_num * s_num
elif operator == "/":
  process = "Division"
  result = f_num / s_num
elif operator == "**":
  process = "Exponentiation"
  result = f_num ** s_num
else:
  process = None
  print("Please enter valid operators.")

if process != None:
  print(f'{process} result = {result}')