# Write a Python function that takes a list 
# and returns a new list with distinct elements from the first list.

numList = input("""Please input your list of numbers here... 
i will do some magic...""")

def distinctList(numList):
    newList = []
    for x in numList:
        if x not in newList:
            newList.append(x)
    return newList

print('Your distinct list is ',distinctList(numList))

    
        