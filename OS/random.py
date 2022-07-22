import random

for n in range(10):
    print(random.random())

print(random.randrange(1, 101))

print(random.randint(1, 101))

fruits = ["apple", "banana", "cherry"]
result = random.choices(fruits, weights=[1, 1, 2], k=10)
print(result)


