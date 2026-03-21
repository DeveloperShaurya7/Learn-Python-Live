marks = float(input("Enter your marks: "))

# Grade A = 100 - 90 
# Grade B = 90 - 75 
# Grade C = 75 - 50 
# Grade D = 50 - 33 
# Grade E = 33 - 0

# Grade logic
if marks >= 90: 
    grade = "A"
elif marks >= 75: 
    grade = "B"
elif marks >= 50: 
    grade = "C"
elif marks >= 33:
    grade = "D"
else:
    grade = "E"

print("Your Grade: ", grade)
