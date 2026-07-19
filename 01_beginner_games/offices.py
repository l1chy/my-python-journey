# Match / Case

cairo = ['Islam Mahfouz', 'Mohamed Mesilhy',
'Hatem Elmaghraby', 'Kareem Embaby']
riyadh = ['Mohamed Gouda', 'Ayman Hamed',
'Seif Ali', 'Adham Wael']
casablanca = ['Ahmed Ashraf', 'Abd El-Rahman Mahrous',
'Islam Sheta', 'Mohamed Medhat', 'Mahmoud Nasser']
dubai = ['Ahmed Alaa', 'Kareem Abd-Elmeged',
'Osama Ashraf', 'Mohamed Mostafa', 'Ahmed Bedeir']

name = input("Enter the name of the office: ").lower()

match name:
    case 'cairo' | 'egypt' | 'eg':
        employees = cairo
    case 'ksa' | 'saudi' | 'riyadh':
        employees = riyadh
    case 'uae' | 'dubai' | 'emirates':
        employees = dubai
    case 'casablanca' | 'morocco':
        employees = casablanca
    case _:
        employees = False
        print(f'Nothing found.')

if employees:
    employees_str = f'{", ".join(employees[:-1])} and {employees[-1]}'
    print(f'Employees in {name.upper()} are: {employees_str}.')