'''
    duck typing : giúp xác định loại đối tượng dựa trên hành vi của nó
    - bạn không cần biết đối tượng là kiểu gì củ thể mà chỉ quan tâm đến hành vi của nó
'''
def Driver(car):
    if hasattr(car, 'driver'):
        car.driver()

class Creta:
    def driver(self):
        print('Creta is driving')

class Mercedes:
    def driver(self):
        print('Mercedes is driving')

c = Creta()
m = Mercedes()

Driver(c)
Driver(m)


def PetLover(pet):
    if hasattr(pet, 'talk'):
        pet.talk()

    if hasattr(pet, 'walk'):
        pet.walk()

class Duck:
    def talk(self):
        print('Duck is talking')
    
    def walk(self):
        print('Duck is walking')

class Dog:
    def talk(self):
        print('Dog is talking')
    

d = Duck()
dog = Dog()

PetLover(d)
PetLover(dog)