num = int(input("Enter a number: "))
reverse = 0

while num !=0:
    digits = num % 10
    reverse = reverse * 10 + digits
    num = num // 10

print("Reversed number: ", reverse)
