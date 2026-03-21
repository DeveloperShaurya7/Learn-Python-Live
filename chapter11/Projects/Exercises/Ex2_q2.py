with open("my_name.txt", "r") as file:
    lines = file.readlines()
    print("Number of lines: ", len(lines))