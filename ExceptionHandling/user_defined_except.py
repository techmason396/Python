class MyError(Exception):
    pass

try:
    raise MyError("Some error")
except MyError as e:
    print(e)
