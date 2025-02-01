#Class and Object
#2. Design a `BankAccount` class with `deposit()` and `withdraw()` methods. Implement logic to prevent overdraft.

class BankAccount:
    def __init__(self,amount):
        self.amount=amount
    def deposit(self,deposit_amount):
        self.deposit_amount=deposit_amount
        self.amount+=deposit_amount
        print()
        print(f"The amount deposited is: {self.deposit_amount} \nFinal balance is {self.amount}")
        print()
    def withdrawn(self,withdrawn_amount):
        self.withdrawn_amount=withdrawn_amount
        if self.amount<withdrawn_amount:
            print("No sufficient amount to withdraw.")
        else:
            self.amount-=withdrawn_amount
            print(f"The {self.withdrawn_amount} amount is withdrawn \nFinal Balance is {self.amount}")

while True:
    print("Select an option:\n 1.Deposit\n 2.Withdraw\n 3.exit")
    bankaccount=BankAccount(1000)
    option=int(input("Enter the option: "))
    if option == 1:
        deposit_amou=int(input("Enter the amount to deposit: "))
        bankaccount.deposit(deposit_amou)
    elif option == 2:
        withdrawn_amou=int(input("Enter amount to with draw: "))
        bankaccount.withdrawn(withdrawn_amou)
    elif option == 3:
         break
    else:
        print("Select correct option")