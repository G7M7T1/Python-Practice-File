class Robots:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __key(self):
        return self.name, self.age, self.address

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Robots):
            return self.__key() == other.__key()
        return NotImplemented

    def __len__(self):
        return len(self.name)

    def __str__(self):
        return f"{self.name} is now {self.age} years old, living in {self.address}"

    def __repr__(self):
        return f"name: {self.name}, age: {self.age}, address: {self.address}"

    def __add__(self, other):
        return self.age + other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age


robot_1 = Robots("will", 25, "Canada")
robot_2 = Robots("Cake", 28, "Canada")
robot_3 = Robots("will", 25, "Canada")

print(robot_1 == robot_3)

print(robot_1.__hash__())

print(len(robot_1))

print(str(robot_1))

print(repr(robot_1))

print(robot_1 + robot_2)

print(robot_1 >= robot_3)
