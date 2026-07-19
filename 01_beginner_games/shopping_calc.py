money = float(input("Enter the amount of money you have: "))
print('-'*20)

first_item = float(input("Enter the price of the first item: "))
second_item = float(input("Enter the price of the second item: "))
third_item = float(input("Enter the price of the third item: "))
remaining = money - (first_item+second_item+third_item)
needed = (first_item+second_item+third_item) - money
print('-'*20)

if remaining >= 0:
    print("Items have been purchased successfully.")
    print(f"The remaining balance is ${remaining}")
else:
    print("Sorry, you don't have enough balance")
    print(f"You need to add an extra ${needed}")