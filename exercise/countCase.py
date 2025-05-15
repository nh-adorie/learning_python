# Write a Python function that accepts a string 
# and counts the number of upper and lower case letters.

sentence = input('Please put your magic sentence here: ')


def countCase(sentence):
    countUpper = 0
    countLower = 0

    # cần đặt biến countUpper và countLower trong này, chứ không phải bên ngoài của def

    for x in sentence:
        if x.islower():
            countLower +=1
        if x.isupper():
            countUpper +=1
        if x.isspace():
            pass
    return countLower, countUpper

lower, upper = countCase(sentence)

print('Your sentence has ',lower,'lower cases and ',upper,' upper cases')

