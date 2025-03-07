class employee:
    def __init__(self,name,salary):
        self._name=name
        self._salary=salary
        self._allowances=int(input("emter the allowances:"))

    def set_salary(self,salary):
        self._salary=salary

    def get_salary(self):
        return self._salary

emp=employee("alice",5000)
print("salary before update:",emp.get_salary())
emp.set_salary(6000)
print("salary after update:",emp.get_salary())