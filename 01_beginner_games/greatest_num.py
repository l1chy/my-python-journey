print(f"Please enter the numbers you want to compare\n{'-'*10}")
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
third = float(input("Enter the third number: "))
print('-'*10)

if first > second:
    if first > third:
        print(f"{first} is the greatest number.")
elif third > second:
    print(f"{third} is the greatest number.")
else:
    print(f"{second} is the greatest number.")