def addition(a, b):
    return a + b

def substraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):   # a -  numerator , b - denominator
    if b == 0:
        return "Cannot divide by Zero"
    return a / b 



# Menu
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")


choice = int(input("Enter your choice: "))

num1 = float(input("Enter first num: "))
num2 = float(input("Enter second num: "))

if choice == 1:
    print("Addition: ", addition(num1, num2))

elif choice == 2:
    print("Substraction: ", substraction(num1, num2))

elif choice == 3:
    print("Multiplication: ", multiplication(num1, num2))

elif choice == 4:
    print("Division: ", division(num1, num2))

else:
    print("Invalid Choice")
 