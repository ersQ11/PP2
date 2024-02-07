class StringManipulator:
    def __init__(self):
        self.user_string = ""

    def getString(self):
        self.user_string = input()

    def printString(self):
        print(self.user_string.upper())

string_obj = StringManipulator()
string_obj.getString()
string_obj.printString()