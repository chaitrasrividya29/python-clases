class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display_info(self):
        print(f"this car is a {self.brand} {self.model}")

car1=car("toyato","corolla")
car2=car("honda","civic")
car1.display_info()
car2.display_info()


