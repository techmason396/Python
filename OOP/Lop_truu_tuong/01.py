'''
    lớp trừu tượng là lớp bạn không thể tạo đối tượng từ đó trực tiếp
    mục đích dùng để định nghĩa các phương thức và thuộc tính chung mà các lớp con cần triển khai
'''

from abc import ABC, abstractclassmethod

class Parent(ABC):
    @abstractclassmethod
    def show(self):
        pass
    
    def display(self):
        print('Parent display')

class Child(Parent):
    def show(self):
        print('Show a child')

c = Child()
c.show()
c.display()