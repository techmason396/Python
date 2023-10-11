'''
    Accessor và mutators là các phương thức dùng để truy cập và thay đổi giá trị của các thuộc tính của một đối tượng
    các phương thức này thường gọi là getter và setter

'''

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    # getter
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    #setter
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age


trung = Person("trung",30)
vui = Person("Vui",27)

print(trung.get_name())
print(trung.get_age())

trung.set_age(32)
trung.set_name("Trung")

print(trung.get_name())
print(trung.get_age())
