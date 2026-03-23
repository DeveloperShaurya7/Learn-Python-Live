# This will not run. It is for eg.
class Student(Person): 
    def __init__(self, name, marks): 
        super().__init__(name) 
        self.marks = marks