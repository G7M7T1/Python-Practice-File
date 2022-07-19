def position(string):
    for num, s in enumerate(string):
        if s == s.upper():
            return s, num
    return -1


print(position("abcd"))
print(position("Abcd"))
print(position("AbCD"))


# Q3.5 --------------------------------
def findAllSmall(lst, num):
    result = []
    for i in lst:
        if i < num:
            result.append(i)
    return result


print(findAllSmall([1, 2, 3], 10))  # returns [1, 2, 3]
print(findAllSmall([1, 2, 3], 2))  # returns [1]
print(findAllSmall([1, 3, 5, 4, 2], 4))  # returns [1, 3, 2]


# Q3.9 --------------------------------
def stars2(num):
    for i in range(1, num + 1):
        print("*" * i)
    for i in range(num - 1, 0, -1):
        print("*" * i)


print(stars2(4))


# Q3.95 --------------------------------
def swap(string):
    result = ""
    for char in string:
        if char == char.upper():
            result += char.lower()
        else:
            result += char.upper()
    return result


print(swap("Aloha"))  # returns "aLOHA"
print(swap("Love you."))  # returns "lOVE YOU."
