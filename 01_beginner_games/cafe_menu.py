drinks = [
# hot drinks
['Tea', 'Herbs', 'Hot Cider', 'Coffee', 'Hot Chocolate'],
# soda
['Coke', 'Pepsi', 'Fanta', 'Sprite', 'Mirinda'],
# juices
['Lemonade', 'Orange Juice', 'Mango Juice',
'Strawberry Juice', 'Apple Juice']
]

print("""
1. Hot Drinks
2. Soda
3. Juices\n""")

category = int(input("Please enter what type of drink you want: "))
menu = f"""
1. {drinks[category-1][0]}
2. {drinks[category-1][1]}
3. {drinks[category-1][2]}
4. {drinks[category-1][3]}
5. {drinks[category-1][4]}\n"""
print(menu)

order_index = int(input("Enter the number of the drink: "))
order = drinks[category-1][order_index-1]
print('-'*50)

print(f"""\nThanks for choosing Lichy's café!\n
Please enjoy your time while we prepare the {order} for you.""")