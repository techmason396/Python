
def devide_two_number():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter b number: "))
        c = a//b
        print(f"{a} / {b} = {c}")
    except (ValueError, ZeroDivisionError) as err:
        print("Value not valid: ",err)
    

devide_two_number()
