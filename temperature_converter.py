# Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

temp = input('Please input the temperature you want to convert ^_^')

# slicing user's input to extract the degree (the number) and the convention (C/F)
degree = int(temp[:-1]) # Phải để degree = int() thì sau đó mới tính toán với nó được
i_convention = temp[-1]

if i_convention.upper() == 'C':
    result = int(round((9 * degree) / 5 + 32))
    o_convention = 'F'

elif i_convention.upper() =='F':
    result = int(round((degree - 32) * 5 / 9))
    o_convention = 'C'
else:
    print('Please input correct temperature ><')

print('The temperature in ', o_convention ,'is ', result)