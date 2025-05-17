# fruits = ["Apple","Peach","Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + "pie")

## Thonny

## HIGHEST SCORE
student_scores = [150,100,200, 120,130,124,126,136,189]
print(sum(student_scores))

total = 0
for score in student_scores:
    total += score
print(total)

max = 0
for score in student_scores:
    if score > max:
        max = score
print(max)

sum100 = 0
for i in range(1,101): # 1 to 101, not including 101
    sum100 +=i
print(sum100)

sum_even = 0
for i in range(2,101,2):
    sum_even+=i
print(sum_even)

sum_odd = 0
for i in range(1,101,2):
    sum_odd +=i
print(sum_odd)
