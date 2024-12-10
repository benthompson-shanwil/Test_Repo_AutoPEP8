import math
GLOBAL_VARIABLE = 'YAY' + str(math.floor(31.34))
class badClass:
    CAP_VAR = 30
    def __init__(self, value):
        self.value = value
    def displayValue(self):
        print("Value is: ", self.value)
def badFunction():
    print("This is bad code")
    if True:
        print("This should be indented properly" )
    for i in range(0, 10):
        print(i)
    print("This should be indented properly EXTREMELY LONG LINE THAjh   "  "   f fytufyfydfsdfsdf uytfftfvT "
          "SHOULD THROW asfdfgsdfgsd fgfgsdfgsdfgsdfdsfgsdg ERROR IF NOT ")
obj = badClass(10)
obj.displayValue()
badFunction()