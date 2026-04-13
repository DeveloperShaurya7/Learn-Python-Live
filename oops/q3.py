class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

b1 = Book("To Kill a Mockingbird", "Harper Lee")
b1.display()
b2 = Book("Python made simple", "Developer Shaurya")
b2.display()