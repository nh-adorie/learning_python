# Scope
cat = 1

def home():
    cat = 2
    print(f"cat inside home: {cat}")

home()
print(f"cat outside home: {cat}")

# Local scope
# Global scope
# Namespace
# Block scope XXXX
# A linter is a tool used in software development 
# to analyze source code and identify issues 
# like errors, bugs, and stylistic inconsistencies.

# prime number
# Prime numbers are numbers that can only be cleanly divided by themselves and 1.

def is_prime(number):
    check = True
    if number <2:
        check = False
    else:
        for i in range(2,number):
            if number % i == 0:
                check = False
    return check
    
print(is_prime(75)) 

# Global constants
PI = 3.14159

def circle():
    global PI
    print(PI)

circle()

def a_function(a_parameter):
    a_variable = 15
    return a_parameter
 
a_function(10)
# print(a_variable)

i = 50
def foo():
    i = 100
    return i
 
foo()
print(i)

def bar():
    my_variable = 9
 
    if 16 > 9:
      my_variable = 16
 
    print(my_variable)
 
bar()






