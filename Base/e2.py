# Q2 --------------------------------
def printEvery3():
    for i in range(1, 89, 3):
        print(i)


printEvery3()


# Q2.5 --------------------------------
def findSmallerTotal(lst, num):
    counter = 0
    for i in lst:
        if i < num:
            counter += i
    return counter


print(findSmallerTotal([1, 2, 3], 3))
print(findSmallerTotal([1, 2, 3], 1))
print(findSmallerTotal([3, 2, 5, 8, 7], 999))
print(findSmallerTotal([3, 2, 5, 8, 7], 0))
