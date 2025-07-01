# Mode:
#   r: đọc file
#   w: ghi file, xóa nội dung cũ
#   a: ghi vào cuối file, không xóa nội dung cũ, không cho đọc
#   a+: ghi vào cuối file, không xóa nội dung cũ, đọc
#   r+: đọc và ghi vào file đã tồn tại
#   w+: đọc và ghi, tạo file mới nếu file chưa tồn tại

# seek(0) sẽ đưa con trỏ chuột về đầu file


with open("./my_file.txt", mode = "a+") as file:
    file.seek(0)
    content = file.read()
    file.write("\nNew text.")
    print(content)

with open("./new_file.txt", mode = "w+") as new_file:
    new_file.write("New file from scratch! ")
    new_file.seek(0)
    print(new_file.read())

# Absolute File Path
# Relative File Path ./ và ../
# Working Directory


