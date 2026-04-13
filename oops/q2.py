class calculator:
    def add(self,a,b):
        return a+b
    
    def subtract(self,a,b):
        return a-b
    
    def multiply(self,a,b):
        return a*b

calc = calculator()
print("Addition:", calc.add(8,3))
print("Subtraction:", calc.subtract(8,3))
print("Multiplication:", calc.multiply(8,3))