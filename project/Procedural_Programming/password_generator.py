import random

print("Welcome to the password generator!")
n_letter = int(input("How many letters would you like in your password? "))
n_symbol = int(input("How many symbols would you like in your password? "))
n_number = int(input("How many number would you like in your password? "))

letters = ['a','b','c','d','e','f','j']
symbols = ['!',')','(','#','$','%','^','&','*','@']
numbers = ['0','1','2','3','4','5','6','7','8','9']

p_letter = []
for i in range (0,n_letter):
    p_letter.append(random.choice(letters))

p_symbol = []
for i in range (0,n_symbol):
    p_symbol.append(random.choice(symbols))

p_number = []
for i in range (0,n_number):
    p_number.append(random.choice(numbers))

password = p_letter + p_symbol + p_number

## Mật khẩu gồm chữ - ký tự - số theo thứ tự

print("Your basic password is: ",''.join(password))
## Cách viết khi chưa biết method .join
# for x in password:
#     print(x,end='')
# print('')


## Mật khẩu gồm chữ - ký tự - số không theo thứ tự

flat_password = []
for nested_list in password:
    for item in nested_list:
        flat_password.append(item)

random.shuffle(flat_password) # xáo trộn lên

print('Your advanced password is: ',''.join(flat_password))

## Cách giải ngắn hơn:
## for i in range (1,n_letter+1):
## password += random.choice(letters)