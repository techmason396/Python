roman = {
    'I': 1,
    'V': 5,
    "X": 10,
    "L": 50,
    "C": 100,
    'D': 500,
    "M": 1000,
}

content = input("Enter your romance code: ").upper()

count = 0

for char in content:
    if char in roman:
        count += roman.get(char)
    else:
        print("Code not valid!")
        break

print(count)