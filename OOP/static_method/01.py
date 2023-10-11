'''
    phương thức tĩnh là phương thức thuộc về lớp chứ không phải thuộc về một đối tượng nào đó
'''

class Rectangle:
    def __init__(self, length, breadth) -> None:
        self.length = length
        self.breath = breadth

    def perimeter(self):
        return 2 * (self.length * self.breadth)
    
    def area(self):
        return self.length * self.breadth

    @staticmethod 
    def issquare(len, bre):
        return len == bre

print(Rectangle(10,20).issquare(10,10))
