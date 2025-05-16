# Write a Python program to construct the following pattern, using a nested for loop.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# 0
# 0 1
# 0 1 2 
# 0 1 2 3
# 0 1 2 3 4 
# 0 1 2 3 4 5 
# 0 1 2 3 4
# 0 1 2 3 
# 0 1 2
# 0 1
# 0

# we print the character row by row


n = 5
for i in range(n):
    for j in range(i):
        print('* ', end="") # end ="" để không xuống dòng
    print('') # để xuống dòng

# i in range (n) --> i: 0, 1, 2, 3, 4
# Vòng 1: i = 0, j = 0, print *
# Vòng 2: i = 1, j = 0, print * / j = 1, print *
# Ctrl / để code <=> comment

for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')

# i in range (n,0,-1) (start, stop, step) --> 5,4,3,2,1 step = -1 là lùi đi 1 số ( •̀ ω •́ )y


# *
# * *
# * * *
# * * * *

# 0
# 0 1
# 0 1 2
# 0 1 2 3

n = 7
for i in range(n):
    for j in range(i+1):
        print('* ', end="")
    print(' ')

#     *
#   * *
# * * *

n = 7
for i in range(n):
    for j in range(i,n): 
        print('  ', end="")
    # print() # không xuống dòng vì còn phải vẽ thêm dấu * bên cạnh khoảng trắng chứ (●'◡'●)

    for j in range(i):
        print('* ', end="")
    print()


# j in range (i) sẽ in ra số dấu từ ít đến nhiều. Vì: i chạy từ 0, 1, 2

# j in range(i,n) sẽ in ra số dấu theo thứ tự nhiều --> ít. Vì: 
# Vòng 1: j in range(1,3) --> j = 0, 1, 2 --> in ra 3 dấu
# Vòng 2: j in range (1,2) --> j = 0, 1 --> in ra 2 dấu

# Hill pattern
#      *
#     * *
#   * * * *

n = 7
for i in range(n):
    for j in range(i,n):
        print("  ", end="")
    for j in range(i):
        print('* ', end="")
    for j in range(i+1):
        print('* ', end="")
    print()