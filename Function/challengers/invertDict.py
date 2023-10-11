myDict = {
    'a': 10,
    'b':20,
    'c':30,
    'd':40
}

def invert_dict(dictargs):
    keys = dictargs.keys()
    values = dictargs.values()
    return dict(zip(values, keys))

print(invert_dict(myDict))