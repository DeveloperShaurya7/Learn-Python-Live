class Dog: 
    def speak(self): 
        print("Bark") 

class Cat: 
    def speak(self): 
        print("Meow") 


# Calling: 
animals = [Dog(), Cat()] 

for animal in animals: 
    animal.speak() 