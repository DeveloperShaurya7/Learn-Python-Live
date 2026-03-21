filename = "myfile.txt"

try:
    file = open(filename, "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("The file does not exist.")

finally:
    try:
      file.close()
      print("File closed successfully.")

    except NameError:
        pass