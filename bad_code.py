class badClass:
    def __init__(self, value):
        self.value = value

    def displayValue(self):
        print("Value is: ", self.value)


def badFunction():
    print("This is bad code")
    if True:
        print("This should be indented properly")
        print("This should be indented properly")
    for i in range(0, 10):
        print(i)


obj = badClass(10)
obj.displayValue()
badFunction()
