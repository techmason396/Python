def stage(age):
    try:
        if age < 13:
            return "Kid"
        elif age >= 13 and age < 19:
            return "Teen"
        elif age >= 19 and age < 50:
            return "Young"
        else:
            return "Old"
    except TypeError as e:
        return "Age not valid, age should is number!"
        

print(stage(49))