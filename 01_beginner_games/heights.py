print("It's time to see heights differently \U0001F603")
height = float(input("Enter height in cm: "))
print('-'*20)

if height >= 200:
    height_class = "very tall."
elif height >= 180:
    height_class = "tall."
elif 160 <= height < 180:
    height_class = "normal."
elif 150 <= height < 160:
    height_class = "short."
else:
    height_class = "very short."
    
print(f"{height} cm is considered {height_class}")