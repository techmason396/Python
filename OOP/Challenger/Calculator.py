class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub( a, b):
        return a - b

    @staticmethod
    def mul( a , b):
        return a * b

    @staticmethod
    def div(a , b):
        return a / b

print(Calculator.add(5,8))
print(Calculator.sub(5,8))
print(Calculator.mul(5,8))
print(Calculator.div(5,8))
    