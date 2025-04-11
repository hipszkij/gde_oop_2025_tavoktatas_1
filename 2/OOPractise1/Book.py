class Book:
    available = 20

    def __init__(self, author, title, publication_year, isbn):
        self.author = author
        self.title = title
        self.publication_year = publication_year
        self.isbn = isbn

    def display_info(self):
        print(f"Author: {self.author}")
        print(f"Title: {self.title}")
        print(f"Publication Year: {self.publication_year}")
        print(f"ISBN: {self.isbn}")

    def get_available(self):
        print(f"Availbale: {self.available}")


book: Book = Book("Teszt author", "Teszt title", 2024, "123456789")
book.display_info()
book.get_available()

Book.available = 19

print("-------")

book2: Book = Book("Teszt author2", "Teszt title2", 1922, "7788994433")
book2.display_info()
book2.get_available()
