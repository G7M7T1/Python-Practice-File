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


# Q2.9 --------------------------------
def stars(num):
    for i in range(num):
        print("*" * (i + 1))


stars(1)
stars(4)


# Q2.95 --------------------------------
def table9to9():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i} * {j} = {i * j}")


table9to9()


# Q --------------------------------
def is_prime(n):
    if n == 1:
        print("False")
        return False

    starter = 2
    while starter < n:
        if n % starter == 0:
            print("False")
            return False
        starter += 1
    print("True")
    return True


is_prime(1)  # returns false
is_prime(5)  # returns true
is_prime(91)  # returns false
is_prime(1000000)  # returns false
