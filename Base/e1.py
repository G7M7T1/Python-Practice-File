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


# Q1.9 --------------------------------
def summ(lst):
    result = 0
    for i in lst:
        result += i
    return result


print(summ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # returns 55
print(summ([]))  # return 0
print(summ([-10, -20, -30]))  # return -60


# Q1.95 --------------------------------
def table(n):
    for i in range(1, 10):
        print(f"{n} * {i} = {n * i}")


print(table(3))


# 3 x 1 = 3
# 3 x 2 = 6
# ...
# 3 x 9 = 27


# Q --------------------------------
def find_min(lst):
    if len(lst) == 0:
        return "undefined"
    result = lst[0]
    for ele in lst:
        if ele < result:
            result = ele
    return result


def my_sort(my_list):
    result_list = []
    while len(my_list) > 0:
        min_element = find_min(my_list)
        result_list.append(min_element)
        my_list.remove(min_element)
    print(result_list)
    return result_list


my_sort([17, 0, -3, 2, 1, 0.5])  # returns [-3, 0, 0.5, 1, 2, 17]
