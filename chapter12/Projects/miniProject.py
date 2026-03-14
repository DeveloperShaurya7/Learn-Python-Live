try:
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your first number: "))

    result = num1 / num2

    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter numeric values")

except ZeroDivisionError:
    print("Error! Division by zero is not allowed")