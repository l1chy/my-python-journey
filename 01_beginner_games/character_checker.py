user_input = input("Enter your input: ")

if user_input.isalnum():
  if user_input.isalpha() and user_input.isupper():
    print("You entered letters\nAll letters are uppercase.")
  elif user_input.isalpha() and user_input.islower():
    print("You entered letters\nAll letters are lowercase.")
  elif user_input.isalpha():
    print("You entered a mix of uppercase and lowercase letters.")
  elif user_input.isnumeric():
    print("You entered a number.")
  else:
    print("You entered a mix of numbers and letters.")
else:
  print("You can only enter numbers and letters.")