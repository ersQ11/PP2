class BankAccount:

    def __init__(self, name, balance, ID):
        self.name = name
        self.balance = balance
        self.ID = ID

    def deposit(self):
        self.depo = int(input("Deposit: "))
        if self.depo > 0:
            self.balance = self.balance + self.depo
            print (f"Your balance is {self.balance}")
        else:
            print("Error: you printed negative sum")

    def withdraw(self):
        self.withd = int(input("Withdraw: "))
        if self.withd > 0:
            if self.balance >= self.withd:
                self.balance = self.balance - self.withd
                print (f"Your balance is {self.balance}")
            else:
                print("You don't have enough money")
        else:
            print("Error: you printed negative sum")

    def oper(self):
        self.operation = int(input("Choose the operation: 1 - check your balance, 2 - deposit, 3 - withdraw, 0 - exit: "))
        if self.operation == 0:
            pass
        elif self.operation == 1:
            print (f"Your balance is {self.balance}")
        elif self.operation == 2:
            self.deposit()
        elif self.operation == 3:
            self.withdraw()
        if self.operation != 0:
            self.oper()

    def get_ID(self, ID):
            return users.get(ID)

users = {1 : BankAccount("Mike", 10000, 1),
        2 : BankAccount("Misha", 102000, 2)}

selected_user = None

while selected_user == None:
    user_ID = int(input("Enter user ID: "))
    selected_user = users.get(user_ID)
    if user_ID == 0:
        break
    elif not selected_user:
        print("User not found. Please try again. If you want to stop the programme, print 0")
    
if user_ID > 0:
    selected_user.oper()