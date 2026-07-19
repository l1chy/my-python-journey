num = float(input("Enter a number: "))
divide = float(input("Enter the number to divide by: "))
result = num / divide
print('-'*20)

if num%divide == 0:
    print(f"The division result is {result:.3f}")
    print(f"{num} is divisable by {divide}")
else:
    print(f"The division result is {result:.3f}")
    print(f"{num} is NOT divisable by {divide}")