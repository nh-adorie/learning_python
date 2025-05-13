# Write a Python program to check if a triangle is equilateral, isosceles or scalene.

# Note :

# An equilateral triangle is a triangle in which all three sides are equal. -- Tam giác đều
# A scalene triangle is a triangle that has three unequal sides. -- Tam giác bình thường
# An isosceles triangle is a triangle with (at least) two equal sides. -- Tam giác cân
# -- Tam giác vuông

a = int(input('First side length is ='))
b = int(input('Second side length is ='))
c = int(input('Third side length is ='))

# Check if a, b, c can create a triangle -- Tổng của hai cạnh bất kỳ phải lớn hơn cạnh còn lại.

if a + b <= c or a + c <= b or b + c <= a:
    print('That is not a triangle :(')
elif a == b == c:
    print('equilateral triangle!')
elif a == b or b == c or a == c:
    print('isosceles triangle')
elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print('right-angled triangle')
else:
    print('scalene triangle')


