# Debugging 
"""
- Describe the problem
- Reproduce the bug
- Play computer
- Fix the Errors 
- Print()
- Using Debugger
- 
"""

try: # Dòng code có thể xảy ra lỗi
    age = int(input("How old are you? "))
except ValueError: # Nếu xảy ra lỗi này thì làm gì
    print("Please input number ") 

def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input("year: "))
print(is_leap(year))


# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 or number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
