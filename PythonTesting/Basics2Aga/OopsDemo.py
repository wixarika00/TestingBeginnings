# classes are user defined blueprint or prototype
# sum, multi, addition, constant
# methods, class variables, instance variables, constructor etc

class Calculator:
    num = 100  # class variables, does not change

    def __init__(self, a, b):
        self.a = a   # instance variable - stored in the class, not object
        self.b = b   # they keep changing for every object creation
        print("I am called automatically")

    def get_data(self):
        print("Let's go")

    def summation(self):
        return self.a + self.b + Calculator.num  # or self.num

obj1 = Calculator(2,3)  # syntax to create objects in python
obj1.get_data()
print(obj1.summation())

obj2 = Calculator(4,5)  # syntax to create objects in python
obj2.get_data()
print(obj2.summation())



