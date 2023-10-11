'''
    self là tham chiếu đến đối tượng hiện tại
'''

class Cuboi:
    def __init__(self, l, b, h):
        self.length = l
        self.breadth = b
        self.height = h
    def lidarea(self):
        return self.length * self.breadth

    def total(self):
        return 2 * (self.length * self.breadth + self.breadth)
    
    def volume(self):
        return self.length * self.breadth * self.height