# Q. Create a program that: 
# • Stores multiple students 
# • Each student has name, age, marks 
# • Displays student details 


students = [] #empty student list

nos = int(input("How many students? "))

for i in range(nos):
    print("Enter details for students", i+1)

    name = input("Enter student name: ")
    age = int(input("Enter student's age: "))
    marks = float(input("Enter student's marks: "))

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)

    print("\n --------- Student Details -----------")

    for s in students:
        print("Name:", s["name"])
        print("Age:", s["age"])
        print("Marks:", s["marks"])

        print()