list1 = ['A','B','C','D','E','A','B','E','B','D','B','E']

result = []

for char in list1:
    if char not in result:
        result.append(char)
        result.append(list1.count(char))

print(result)