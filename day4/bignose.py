class parent:
    def __init__(self):
        self.bigNose="7cm"

    def display_parent(self):
        print("this is parent class")
class child(parent):
    def display_child(self):
        print("this is child class")
c=child()
c.display_parent()
c.display_child()
print(c.bigNose)
