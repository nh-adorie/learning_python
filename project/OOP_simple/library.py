# Create a library management program

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self): # tự động biểu diễn object dưới dạng chuỗi khi được gọi trong print
        if self.is_borrowed == False:
            status = "Avalable"
        else:
            status = "Borrowed"
        return f"\nTitle: {self.title}\nAuthor: {self.author} \nStatus: {status}"
    
    def is_borrowed(self):
        self.is_borrowed = False
    
    def borrow_book(self):
        if self.is_borrowed == False: # sách chưa được mượn
            self.is_borrowed = True # chuyển trạng thái thành "Đã cho mượn"
            return True # cho mượn sách
        else:
            return False # không thể cho mượn sách

    def return_book(self):
        if self.is_borrowed == False: # sách chưa được mượn
            return False # không thể trả lại sách
        else:
            self.is_borrowed = False # chuyển trạng thái thành "Có sách"
            return True # có thể trả lại sách

    # def display_book_info(self): 
    #     print(f"Title: {self.title} by {self.author}")
    # khi sử dụng cách này, print(book) sẽ không cho kết quả là string
    # mà sẽ nhận được dạng: <__main__.Book object at 0x70967a103940>
    
class Library:
    def __init__(self):
        self.list_of_books = []
    
    def add_book(self,book):
        self.list_of_books.append(book)

    def __iter__(self): # method này sẽ tự động chạy khi 1 object tạo ra từ class library bị gọi trong vòng lặp
        return iter(self.list_of_books)

def find_book_by_title(self, title):
        for book in self.list_of_books:
            if book.title.lower() == title.lower():  # Không phân biệt hoa thường
                return book
        return None  # Trả về None nếu không tìm thấy
  
book_dicts = {
    "The Little Prince": "Antoine de Saint-Exupéry",
    "The Story of a Seagull and the Cat Who Taught Her to Fly": "Luis Sepúlveda",
    "Confessions": "Jean-Jacques Rousseau",
    "Norwegian Wood": "Haruki Murakami"
}

library = Library()

for title, author in book_dicts.items():
    book = Book(title,author)
    library.add_book(book)


print("Welcome to Adorie Magical Library\nHere is our book list: ")
for book in library: # vì class Library có method __iter__ nên có thể lặp qua được
    print(book) # vì class Book có method __str__ nên có thể biến obj thành str 

book_choice = input("\nWhat do you want to borrow? ")
book = library.find_book_by_title(book_choice)
if book:
    print(f"Found: {book}")
else:
    print(f"Book '{book_choice}' not found")


