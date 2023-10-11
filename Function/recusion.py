

def factory(n):
    if n == 0:
        return 1
    return n * factory(n-1)

result = factory(5)
print(result)
    