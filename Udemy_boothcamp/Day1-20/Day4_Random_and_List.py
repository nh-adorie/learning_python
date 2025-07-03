## deterministic
## pseudorandom number generators
## modules

import random

random_interger = random.randint(1,100)
print(random_interger)

random_number_0_to_100 = random.random()*100
print(random_number_0_to_100)

random_float = random.uniform(1,100)
print(random_float)

random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")

## LIST: có thứ tự, có thể sửa, có thể thêm

fruits = ["mango","apply","banana"]
fruits[1] = "apple"
fruits.append("strawberry")
print(fruits)

## WHO PAY THE BILL?
friends = ["Alice","Bob","Charlie","David","Emanuel"]
who = random.randint(0,4)
print(friends[who]," will pay the bill")

print(random.choice(friends)," will pay the bill")


# Kale: cải xoăn
# Nectarines: xuân đào
# Celery: cần tây
dirty_fruits = ["Strawberries","Apple","Grapes","Peaches","Cherries","Pears","Tomatoes"]
dirty_vegetables = ["Spinach","Kale","Nectarines","Celery","Potatoes"]
dirty_dozen = [dirty_fruits, dirty_vegetables] # nested list
print(dirty_dozen)

print(dirty_dozen[1][1]) # print ra giá trị tại index 1 của list tại index 1









