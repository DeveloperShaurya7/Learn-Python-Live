class Student: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

# Creating objects of the Student class: 
s1 = Student("Ravi", 20) 
s2 = Student("Priya", 22) 

# Accessing attributes: 
print(s1.name, s1.age) 
print(s2.name, s2.age) 