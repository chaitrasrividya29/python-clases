class  emp:
    def __init__(self,salary,name):
        self.name=name
        self.salary=salary
    
    def display(self):
        print("names",self.name)
        print("salary",self.salary)

detail= emp([2000,5000,8000],['a','b','c'])
detail.display()