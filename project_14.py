print("This is Banking system.\nPlease choose from 'Deposit' or 'Withdraw'\nWhen you are done you can choose 'quit'!\n")
class Bank:

    def __init__(self, initialBalance=0.00):
        self.balance = initialBalance

    def logTransaction(self, transaction_string):
        with open("banking.txt", 'a') as file:
            file.write(f"{transaction_string} \t\t\tBalance: {self.balance}\n")

    def withdrawal(self, amount):
        amount = float(amount)
        if amount: 
            self.balance = self.balance - amount
            self.logTransaction(f"Withdrew {amount}")

    def deposit(self, amount):
        amount = float(amount)
        if amount:
            self.balance = self.balance + amount
            self.logTransaction(f"Deposited {amount}")


account = Bank(0.00)
while True:
    
    action = input("What kind of action do you want to take?\n")
    if action in ["withdraw", "deposit","quit"]:
        if action == "withdraw":
            amount= input("Enter the amount to withdraw: ")
            account.withdrawal(amount)
        
        elif action == "deposit":
            amount = input("Enter the amount you want to deposit: ")
            account.deposit(amount)

        elif action == "quit":
            quit()

        print("Your balance is", account.balance)
    else:
        print("Not a valid action. Try again!")

