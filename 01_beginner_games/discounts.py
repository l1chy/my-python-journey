sales_70 = ['070', '170', '270', '370', '470']
sales_50 = ['050', '150', '250', '350', '450']
sales_30 = ['030', '130', '230', '330', '430']

code = input("Enter the code of the item: ")
price = float(input("Enter the price of the item: "))

if code in sales_70:
  discount = price * 0.3
  stamp = "70%"
elif code in sales_50:
  discount = price * 0.5
  stamp = "50%"
elif code in sales_30:
  discount = price * 0.7
  stamp = "30%"
else:
  discount = price * 1
  stamp = ""

print('-'*10)
print(f"The Item Code-{code} after {stamp} discount is {discount}")