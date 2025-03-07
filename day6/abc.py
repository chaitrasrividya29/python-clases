from abc import ABC, abstractmethod
class father(ABC):
    @abstractmethod
    def disp(self):
       pass
    def show(self):
       print("Concrete Method")
class son(father):
    def disp(self):
      print("son is implementing the abstract method")
      
class daughter(father):
   def disp(self):
      print("daughter is implementing the abstract method)

s=son()
s.disp()
s.show()
      
d=daughter()
s.disp()
s.show()
      