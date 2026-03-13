# Q. Create a program that: 
# • Takes note input from the user 
# • Saves it to a file 
# • Displays all saved notes 

file_name = "notes.txt"

note = input("Enter your note: ")

file = open(file_name, "a")
file.write(note + "\n")
file.close()

print("Note saved successfully! \n")

print("--------- Saved Notes ------------")
file = open(file_name, "r")
content = file.read()
print(content)
file.close()
