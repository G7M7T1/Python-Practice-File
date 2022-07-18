# Q1 --------------------------------
def printMany():
    for i in range(1, 100):
        print(i)


printMany()


# Q1.5 --------------------------------
def find_small_count(lst, num):
    for i in lst:
        if i < num:
            return 1
        else:
            return 0


print(find_small_count([1, 2, 3], 2))
print(find_small_count([1, 2, 3, 4, 5], 0))


