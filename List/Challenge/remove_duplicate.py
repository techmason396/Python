
numbers = [3,5,9,8,3,4,5,9,6,3,7,2]

result = []
for number in numbers:
    if number not in result:
        result.append(number)

print(result)