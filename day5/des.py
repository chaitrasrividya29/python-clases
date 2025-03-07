# class destruct:
#     def __init__(self):
#         print("you are in constructor")
#     def __del__(self):
#          print("you are in de7structor")

# ab=destruct()
# del ab

class example:
    def __init__(self,name):
        print(f"first constructor name: {name}")
    def _init_(self,rno):
        print(f"second constructor name: {rno}")
obj=example(87)


class destructorex:
    def _init_(self,name):
        self.name=name
        print(f"object {self.name} is created.")
    def _del_(self):
        print(f"object {self.name} is destroyed")
obj=destructorex("sample")
del obj