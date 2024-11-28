class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")

my_book = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
my_book.display_info()
