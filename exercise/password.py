# Write a Python program to check the validity of passwords input by users.

# Validation :

# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

print("""Password rule:
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.

""")

# Dùng 3 dấu nháy để viết xuống dòng

password = input('Please input your password with the above condition:')

if len(password) < 6 or len(password) > 16:
     "Password must be between 6 - 16 characters"

has_lower = False
has_upper = False
has_digit = False
has_special = False

for char in password:
    if char.islower():
        has_lower = True
    
    elif char.isupper():
        has_upper = True

    elif char.isdigit():
        has_digit = True
    
    elif char in '$#@':
        has_special = True

if has_upper and has_lower and has_digit and has_special:
        print('Good password')
else:
        print('Please input another password')

