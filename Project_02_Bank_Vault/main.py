class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Error: Deposit amount must be positive.")
    def withdraw(self,amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print(f"Error: Insufficient funds. You tried to withdraw {amount} but only have {self.__balance}.")
        else:
            print("Error: Withdrawal amount must be positive.")
    def balance(self):
        return self.__balance



my_account = BankAccount("Benjamin", 6000)
my_account.deposit(500)
my_account.withdraw(200)
print(f"Your account balance is {my_account.balance()}")