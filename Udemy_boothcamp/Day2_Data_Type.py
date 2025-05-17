# DATA TYPE
# Subscripting
print('Hello'[4])

# Concatenation
print("123"+"456")

# Interger = whole number
print(123+456)

# Large Intergers
print(123_456_789) # Là số 123,456,789

# Float  = floating point number
print(3.14)

# Boolean
print(True)
print(False)

# TYPE ERROR
print(type("Hello"))
print(type(123))
print(type(1.23))
print(type(True))

print(int("123")+456)

int()
float()
str()
bool()

# name = input('Input your name: ')
# count = len(name)
# print('Length of your name: ',count)

## MATHEMATICAL OPERATORS
print(3 * 2)
print(5 / 3) 
print(5 // 3)
print(2 ** 2)
print(7 % 3) #remainder


## NUMBER MANIPULATION

bmi = 48 / 1.55**2
print(bmi)
print(round(bmi))
print(round(bmi,2))

score = 0
score +=1 
print(score)

# f-strings
print('Your score is ',score)
print(f"Your score is {score}")


## PROJECT 1: TIP CALCULATOR
print("Welcome to the tip calculator!")
total = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bills? "))

pay = (total + total*tip/100)/people
print("Each person should pay: ",pay)
