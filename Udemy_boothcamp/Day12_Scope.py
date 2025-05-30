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





