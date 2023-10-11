
class People:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def infor(self):
        print(f"My name is {self.name}, age is {self.age}")

# kế thừa
class Student(People):
    def __init__(self, name, age, code) -> None:
        super().__init__(name, age)
        self.code = code

    def infor(self):
        print(f"My name is {self.name}, age is {self.age} and my code is {self.code}")


st1 = Student("Trung",10, "qt112")
st1.infor()