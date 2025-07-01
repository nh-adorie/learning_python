import os

# lấy đường dẫn thư mục đang làm việc (của file main.py này này)
current_path = os.getcwd()
print(current_path)

letter_path = "/workspaces/learning_python/project/Mail_Merge/Input/Letters/starting_letter.txt"
names_path = "/workspaces/learning_python/project/Mail_Merge/Input/Names/invited_names.txt"

# đọc file starting_letter
with open(letter_path) as letter_file:
    letter_template = letter_file.read()

# đọc file invited_names
with open(names_path) as names_file:
    names_list = names_file.readlines()

# print(type(names_list)) 
# Khi sử dụng read thì names_list là str // Khi sử dụng readlines thì names_list là list

# thay thế tên trong names_list vào letter_template
for name in names_list:
    replace_name = name.strip()
    personized_letter = letter_template.replace("[name]", replace_name)

    # lưu thành file mới
    output_path = "/workspaces/learning_python/project/Mail_Merge/Output/Ready_to_send"
    personized_path = os.path.join(output_path,f"letter_for_{replace_name}")
    with open(personized_path, "w") as output_letter: 
        # chỗ này cần để mode w để tạo file mới
        output_letter.write(personized_letter)