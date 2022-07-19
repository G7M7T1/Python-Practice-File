import random

secret = random.randint(0, 100)
min_value = 0
max_value = 100

while True:
    input_number = input("Make your guess number 1 - 100: \n")
    if int(input_number) < min_value or int(input_number) > max_value:
        print("You Have To Enter Number 0 - 100")
        continue
    if int(input_number) == secret:
        print(f"The Secret Is {secret}, You Got It")
        break
