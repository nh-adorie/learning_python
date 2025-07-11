# Mode:
#   r: đọc file
#   w: ghi file, xóa nội dung cũ
#   a: ghi vào cuối file, không xóa nội dung cũ, không cho đọc
#   a+: ghi vào cuối file, không xóa nội dung cũ, đọc
#   r+: đọc và ghi vào file đã tồn tại
#   w+: đọc và ghi, tạo file mới nếu file chưa tồn tại

# seek(0) sẽ đưa con trỏ chuột về đầu file

# Absolute File Path
# Relative File Path ./ và ../
# Working Directory

import os

# Lấy đường dẫn thư mục chứa file này (main.py)
base_path = os.path.dirname(os.path.abspath(__file__))

# Tạo đường dẫn đầy đủ đến my_file.txt và new_file.txt trong cùng thư mục với main.py
my_file_path = os.path.join(base_path, "my_file.txt")
new_file_path = os.path.join(base_path, "new_file.txt")

with open(my_file_path, mode="a+") as file:
    file.seek(0)
    content = file.read()
    file.write("\nNew text.")
    print(content)

with open(new_file_path, mode="w+") as new_file:
    new_file.write("New file from scratch! ")
    new_file.seek(0)
    print(new_file.read())
