class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  # Mặc định sách chưa mượn

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"Title: {self.title}\nAuthor: {self.author}\nStatus: {status}"

    def borrow_book(self):
        if self.is_borrowed: 
            return False
        self.is_borrowed = True
        return True

    def return_book(self):
        if not self.is_borrowed:
            return False
        self.is_borrowed = False
        return True

class Library:
    def __init__(self):
        self.list_of_books = []

    def add_book(self, book):
        self.list_of_books.append(book)

    def __iter__(self):
        return iter(self.list_of_books)

    def find_book_by_title(self, title):
        for book in self.list_of_books:
            if book.title.lower() == title.lower():  
                return book
        return None

    def borrow_book_by_title(self, title):
        book = self.find_book_by_title(title)
        if book is None:
            return f"Error: Book '{title}' not found in the library."
        if book.borrow_book():
            return f"Here is your book"
        return f"Sorry, it is already borrowed."

# Danh sách sách
book_dicts = {
    "The Little Prince": "Antoine de Saint-Exupéry",
    "The Story of a Seagull and the Cat Who Taught Her to Fly": "Luis Sepúlveda",
    "Confessions": "Jean-Jacques Rousseau",
    "Norwegian Wood": "Haruki Murakami"
}

def main():
    library = Library()
    for title, author in book_dicts.items():
        book = Book(title, author)
        library.add_book(book)


    print("Welcome to my library")
    print("Enter the title of the book to borrow, or 'quit' to exit.")
    while True:
        title = input("Enter book title: ").strip()
        if title.lower() == "quit":
            print("Goodbye ~ ")
            break
        result = library.borrow_book_by_title(title)
        print(result)
        print("\nEnter another book title or 'quit' to exit.")

if __name__ == "__main__":
    main()