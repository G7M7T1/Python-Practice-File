def divide_1(a, b):
    if type(a) == int and type(b) == int:
        if b != 0:
            return a / b
        else:
            return "Can't not divide by 0"
    else:
        return "Invalid argument type!"


def divide_2(a, b):
    if type(a) != int or type(b) != int:
        raise ValueError("Not Valid Number")

    if b == 0:
        raise ZeroDivisionError("Can't not divide by 0")

    return a / b


try:
    print(divide_2(10, "hello"))

except Exception as e:
    print(e)
