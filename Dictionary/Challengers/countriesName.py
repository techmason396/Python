countries = {
    'A': ['America','Alaska','Argentina'],
    'B': ['Bhutan','Brazil','Bahrain'],
    'C': ['China','Costa Rica','Cuba']
}

name = input('Country name: ').capitalize()

first_char_name = name[0]

if first_char_name in countries:
    countries[first_char_name].append(name)
else:
    countries[first_char_name] = [name]

print(countries)

