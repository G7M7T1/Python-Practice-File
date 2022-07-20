class Employee:
    def __init__(self):
        self.income = 0
        self.__tax = 0

    def earn_money(self, money):
        self.income += money

    def get_tax(self):
        self.__tax += self.income * 0.15
        return self.__tax

    @property
    def tax_amount(self):
        return self.income * 0.15


wang = Employee()
wang.earn_money(3500)
print(wang.tax_amount)
print(wang.get_tax())

