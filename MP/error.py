# LBYL
def safe_divide_1(x, y):
    if y == 0:
        print("Can't not do it")
        return None
    else:
        return x / y


# EAFP
def safe_divide_2(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Can't not do it")
        return None
