class Book:
    def __init__(self, title, author, isbn, num_pages, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.num_pages = num_pages
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Number of Pages: {self.num_pages}")
        print(f"Price: ${self.price:.2f}")


class ReferenceBook(Book):
    def __init__(self, title, author, isbn, num_pages, price, ref_type):
        super().__init__(title, author, isbn, num_pages, price)
        self.ref_type = ref_type

    def display_details(self):
        super().display_details()
        print(f"Reference Type: {self.ref_type}")


class FictionBook(Book):
    def __init__(self, title, author, isbn, num_pages, price, genre):
        super().__init__(title, author, isbn, num_pages, price)
        self.genre = genre

    def display_details(self):
        super().display_details()
        print(f"Genre: {self.genre}")


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.title] = book
        print(f"Book '{book.title}' added to the library.")

    def display_all_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books.values():
                book.display_details()

    def search_by_title(self, title):
        if title in self.books:
            self.books[title].display_details()
        else:
            print(f"Book '{title}' not found.")

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print(f"Book '{title}' removed.")
        else:
            print(f"Book '{title}' not found in the library.")


# Interaction with the Library Management System
my_library = Library()

while True:
    print("\nLibrary Management System Menu:")
    print("1. Add a book")
    print("2. Display all books")
    print("3. Search for a book by title")
    print("4. Remove a book")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        book_type = input("Enter book type (R for Reference, F for Fiction): ")
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        num_pages = int(input("Enter number of pages: "))
        price = float(input("Enter price: "))

        if book_type.upper() == 'R':
            ref_type = input("Enter reference type: ")
            book = ReferenceBook(title, author, isbn, num_pages, price, ref_type)
        elif book_type.upper() == 'F':
            genre = input("Enter genre: ")
            book = FictionBook(title, author, isbn, num_pages, price, genre)
        else:
            print("Invalid book type.")

        my_library.add_book(book)

    elif choice == '2':
        my_library.display_all_books()

    elif choice == '3':
        search_title = input("Enter title to search: ")
        my_library.search_by_title(search_title)

    elif choice == '4':
        remove_title = input("Enter title to remove: ")
        my_library.remove_book(remove_title)

    elif choice == '5':
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
