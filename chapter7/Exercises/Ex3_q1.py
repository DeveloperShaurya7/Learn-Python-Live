myList = [1, 2, 44, 72, 43, 97, 12]

even = 0 
odd = 0

for i in myList:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Total even numbers: ", even)
print("Total odd numbers: ", odd)