class shape :
    def area (self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14* self.radius ** 2

class square(shape):
    def __init__(self,side):
     self.side=side
    def area(self):
        return self.side*self.side
c=circle(4)
s=square(5)
print("area circle",c.area())    
print("area square",s.area())    