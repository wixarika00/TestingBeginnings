from OopsDemo import Calculator

class ChildImp(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def get_complete_data(self):
        return self.num2 + self.num + self.summation()

obj = ChildImp()
print(obj.get_complete_data())
