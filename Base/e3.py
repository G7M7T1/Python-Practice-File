def position(string):
    for num, s in enumerate(string):
        if s == s.upper():
            return s, num
    return -1


print(position("abcd"))
print(position("Abcd"))
print(position("AbCD"))
