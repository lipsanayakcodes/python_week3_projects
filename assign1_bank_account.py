#Create class with methods: deposit, withdraw, display balance.

class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully.")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    # Display balance
    def display_balance(self):
        print("\n----- Account Details -----")
        print("Account Holder:", self.account_holder)
        print("Current Balance:", self.balance)


# Take input from user
name = input("Enter account holder name: ")
initial_balance = float(input("Enter initial balance: "))

# Create object
account = BankAccount(name, initial_balance)

while True:
    print("\n===== Bank Account =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == "3":
        account.display_balance()

    elif choice == "4":
        print("Thank you for using Bank Account System!")
        break

    else:
        print("Invalid choice. Please try again.")