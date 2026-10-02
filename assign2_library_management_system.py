#Library Management System (OOP) :
  #  Add/remove books, issue/return books.

class Library:

    def __init__(self):
        self.books = []

    # Add a book
    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    # Remove a book
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book removed successfully.")
        else:
            print("Book not found.")

    # Issue a book
    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book issued successfully.")
        else:
            print("Book is not available.")

    # Return a book
    def return_book(self, book):
        self.books.append(book)
        print("Book returned successfully.")

    # Display books
    def display_books(self):
        if self.books:
            print("\n----- Available Books -----")
            for book in self.books:
                print(book)
        else:
            print("No books available.")


# Create library object
library = Library()

while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        library.add_book(book)

    elif choice == "2":
        book = input("Enter book name to remove: ")
        library.remove_book(book)

    elif choice == "3":
        book = input("Enter book name to issue: ")
        library.issue_book(book)

    elif choice == "4":
        book = input("Enter book name to return: ")
        library.return_book(book)

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")