# format name
def format_name(first_name,last_name):
    """ Take the first and last name
    and format it to retun the title case version 
    of the name """
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(format_name("chICken","adOrie"))

# Leap Year

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False

    

# chia hết cho 4 nhưng không chia hết cho 100 hoặc chia hết cho 400 thì là năm nhuận
# chỉ chia hết cho 100 thì không là năm nhuận

# Docstring

def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2
 
print(add(2, multiply(5, divide(8, 4))))

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)

def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))