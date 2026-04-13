class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def add_bonus(self):
        total_salary = self.salary + self.bonus
        print("Total Salary with Bonus:", total_salary)

m1 = Manager("Shaurya", 50000, 10000)
m1.display()
m1.add_bonus()