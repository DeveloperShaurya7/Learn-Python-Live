marks = float(input("Enter your marks: "))

# Grade A = 100 - 90 - pass
# Grade B = 90 - 75 - pass
# Grade C = 75 - 50 - pass
# Grade D = 50 - 33 - pass
# Grade E = 33 - 0 - fail

if(marks >= 90):
    grade = "A"
elif (marks >= 75):
    grade = "B"
elif (marks >= 50):
    grade = "C"
elif(marks >= 33):
    grade = "D"
else:
    grade = "E"

print("Your Grade: ", grade)

if marks >= 33: 
    print("Pass")
else:
    print("fail") 
