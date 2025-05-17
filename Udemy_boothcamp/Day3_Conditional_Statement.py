## ROLLERCOSTER 

print("Welcome to the rollercoster!")
height = int(input("What is your height in cm? "))
bill = 0
if height > 120:
    print('You can ride the rollercoster!')
    age = int(input("What is your age? "))
    if age <12:
        bill = 5
    elif age >=12 and age <18:
        bill = 7
    else: 
        bill = 12
    
    photo = input('Do you want to take a photo? Y for Yes and N for No ')
    if photo == "Y":
        bill +=3
    # không có else cũng được

    print("Your bill is ",bill)
        

    
else:
    print("Sorry you have to grow taller before you can ride.")

# Comparison Operator: 
# > 
# < 
# >= 
# <= 
# == 
# !=

## CHECK ODD OR EVEN
def check_odd_even(num):
    if num % 2 == 0:
        return 'Even number'
    return 'Odd number'

num = int(input("What is your number? "))
print("Your number is ",check_odd_even(num))


## PIZZA ORDER
print("Welcome to Pizza Delivery")
size = input("What size do you want: S, M, L? ")
pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill+=15
    if pepperoni == "Y":
        bill+=2

elif size == "M":
    bill+=20
    if pepperoni == "Y":
        bill+=3
else:
    bill+=25
    if pepperoni == "Y":
        bill+=3

if extra_cheese == "Y":
    bill+=1

print("Your final bill is ",bill, "$")


