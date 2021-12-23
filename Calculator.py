def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculator():
    num1 = float(input("what is the first number? "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        symbols = input("what is the symbol key? ")
        num2 = float(input("what is the second number? "))
        answer = operations[symbols](num1, num2)
        print(f"{num1} {symbols} {num2} = {answer}")

        if input(f"anser is {answer} you can y to continue n new calculator") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
