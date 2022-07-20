class Robot:
    robot_type = "Bot"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self, hours):
        print(f"{self.name} is going to sleep for {hours} hours")


my_robot_1 = Robot("Will", 25)
print(my_robot_1.age)
print(my_robot_1.name)

my_robot_1.sleep(60)
