# Import Class
from book_store import BookStore
from app import Management
from book import Book
from raw_data import books_data

# Lấy dữ liệu từ raw data
store = BookStore()
for book in books_data:
    add_book = Book(book["id"],book["title"],book["author"],book["price"],book["quantity"])
    store.add_book(add_book)
print("\nBooks available in the store:\n")
store.display_book_list()

# Chạy chương trình
management_app = Management(store)
management_app.main_menu()