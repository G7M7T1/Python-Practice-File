class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(f"{self.name} is sleeping...")


class Student(People):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id


student_1 = Student("Will", 25, 10001)
print(student_1.name)

student_1.sleep()
