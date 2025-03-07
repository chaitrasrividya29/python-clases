class example:
    def __init__(self,std_name,**kwargs):
        self.std_name=std_name
        if "name" in kwargs and "age" in kwargs:
            print(f"hello {kwargs['name']}, you are {kwargs['age']} years old")
        elif "name" in kwargs:
            print(f"hello {kwargs['name']}")
        self.xfield=kwargs['name']
obj1=example("sri",name="chaitra",age=21)