'''
    ghi đè phương thức là lớp con có thể định nghĩa lại phương thức đã được định  nghĩa trong lớp cha
'''

class Animal:
    def speak(self):
        print("Animal speak")

class Dog(Animal):
    def speak(self, sound):
        print(f"Dog speak is {sound}")

a = Animal()
d = Dog()
a.speak()
d.speak('gau gau')