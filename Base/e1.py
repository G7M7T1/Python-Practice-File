# Q1 --------------------------------
def printMany():
    for i in range(1, 100):
        print(i)


printMany()


# Q1.5 --------------------------------
def find_small_count(lst, num):
    counter = 0
    for i in lst:
        if i < num:
            counter += 1
    return counter


print(find_small_count([1, 2, 3], 2))
print(find_small_count([1, 2, 3, 4, 5], 0))


