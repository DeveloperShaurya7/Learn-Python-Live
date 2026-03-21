try:
    filename = input("Enter the filename: ")
    with open(filename, 'r') as file:
        content = file.read()
        print(content)  

except FileNotFoundError:
    print("The file does not exist. Please check the filename and try again.")