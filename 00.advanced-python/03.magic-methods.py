# magic methodlar "__" ile çevrilidir. bunlara dunder method da denir.
# örn "__init__()"

# __str__() # objenin okunabilir bir tanımını oluştururuz. 

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

    def __str__(self):
        return f"Employee(name={self.name}, last={self.last}, age={self.age}, pay={self.pay})"
        # return "merhaba"

    def __add__(self, other): # "+" operatörüne girince objenin nasıl davranacağına karar veriyor.
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.name)
    

emp1 = Employee("john", "doe", 30, 10000)
print(emp1)

emp2 = Employee("jane", "doe", 32, 20000)
print(emp1 + emp2)

print(len(emp1))