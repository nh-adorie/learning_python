from book_store import Book, BookStore
from raw_data import books_data

# Lấy dữ liệu từ raw data
store = BookStore()
for book in books_data:
    book = Book(books_data["id"],books_data["title"],books_data["author"],books_data["price"],books_data["quantity"])
    store.append(book)

store.display_book_list()

