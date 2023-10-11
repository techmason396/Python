birthdays = {
    'Sachin':'03/14/2003',
    'Carl':'01/17/2001',
    'Khan':'12/10/2006',
    'Donald':'06/14/2010',
    'Rohan':'01/06/2005',
}

name = input("Enter name search birthday: ")
if name in birthdays:
    birthday = birthdays.get(name)
    print( f"name : {name} birthday is {birthday}")
else:
    print(f"{name} is not found!")
