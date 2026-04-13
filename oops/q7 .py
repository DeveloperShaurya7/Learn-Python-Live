class Library:
    def __init__(self):
        self.books = [] 
        self.issued_books = {}
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' added to the library.")

    def issue_book(self, book, user):
        if book in self.books:
            self.books.remove(book)
            self.issued_books[book] = user
            print(f"Book '{book}' issued to {user}.")
        else:
            print(f"Book '{book}' is not available in the library.")

    def return_book(self, book):
        if book in self.issued_books:
            user = self.issued_books.pop(book)
            self.books.append(book)
            print(f"Book '{book}' returned by {user}.")
        else:
            print(f"Book '{book}' was not issued from the library.")

    def display_books(self):
        print("Availabe Books:", self.books)


lib = Library()
lib.add_book("Python made simple")
lib.add_book("Data Structures and Algorithms")

lib.display_books()

lib.issue_book("Python made simple", "Shaurya")
lib.issue_book("Data Structures and Algorithms", "Shanti")
lib.return_book("Python made simple")   