class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("insufficient amount please try again!!!")
    def withdraw(self,amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Insulficient amount")
        else:
            print("Check the amount entered")
    def balance(self):
        return self.__balance



my_account = BankAccount("Benjamin", 6000)
my_account.deposit(500)
my_account.withdraw(200)
print(f"Your account balance is {my_account.balance()}")