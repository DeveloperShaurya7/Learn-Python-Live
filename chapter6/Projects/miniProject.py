# if (userNum == secret_num)

# 1. variables 
# 2 input output logic
# 3. Sytax error
# 4 Run (error - hit & trial method)

#  For  - Fix number of loops | You know the looping number
#  While  - Not a fix num of loops | You do not know how much it will run

# import random #import random
secret_num = 25 #random.randint(1,10)

while True:
    userGuessNum = int(input("Guess the number: ")) #Takes input from the user 

    if userGuessNum == secret_num:
        print("Correct! You won.") #If condition is True
        break
    else:
        print("Wrong! Try again. ") #If condition is False
