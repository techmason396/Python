print('before try')
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter b number: "))
    c = a// b
except (ZeroDivisionError, ValueError) as err:
    print(err)
else:
    print(f"{a} / {b} = {c}")
finally:
    print("Ending")