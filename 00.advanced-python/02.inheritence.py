class Employee:

    raise_percent = 1.05
    num_emp = 0

    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay
        Employee.num_emp += 1

    def apply_raise(self):
        self.pay = self.pay * self.raise_percent

emp1 = Employee("oguzhan", "kuslar", 23, 1000)

class IT(Employee):
    raise_percent = 1.2
    # subclass'ta yaptığımız değişiklik parent class'ı etkilemez.
    def __init__(self, name, last, age, pay, lang):
        super().__init__(name, last, age, pay)
        self.lang = lang

emp2 = IT("dogukan", "kuslar", 27, 5000, "eng")
emp2.apply_raise()
print(emp2.pay)

class HR(Employee):
    raise_percent = 1.3
    def __init__(self, name, last, age, pay, experience):
        super().__init__(name, last, age, pay)
        self.experience = experience

    def print_exp(self):
        print(f"This employee has {self.experience} years of experience.")

emp3 = HR("yusuf", "trasci", 27, 10000, 12)
emp3.print_exp()

 
print(isinstance(emp1, HR))
print(isinstance(emp3, HR))
print(isinstance(emp3, Employee))

print(issubclass(IT, Employee))
print(issubclass(IT, HR))