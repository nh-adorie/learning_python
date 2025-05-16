
numList = input('Please give me your list of numbers:')

newList = []
for i in numList:
    newList.append(int(i))

def sumList(newList):
    result = 0
    for x in newList:
        result += x
    return result

print('Your list of numbers total sum is:', sumList(newList))
