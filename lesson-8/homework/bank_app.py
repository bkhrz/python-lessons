import json
import random

class Account:

    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f'Deposit added. New balance {self.balance}')
        else:
            print('Please, enter a positive number')

    def withdraw(self, amount: float):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f'Amount withdrew. New balance {self.balance}')
            else:
                print('Insufficient balance')
        else:
            print('Please, enter a positive number')

    def __str__(self):
        return f"""Account number: {self.account_number}
Name: {self.name}
Balance: {self.balance}"""

class Bank:
    def __init__(self, file='accounts.json'):
        self.accounts = {}
        self.file = file
        self.load_from_file()

    def save_to_file(self):
        with open(self.file, 'w') as f:
            json.dump({int(acc_num): vars(acc) for acc_num, acc in self.accounts.items()}, f)

    def load_from_file(self):
        try:
            with open(self.file, 'r') as f:
                data = json.load(f)
                self.accounts = {int(acc_num): Account(**details) for acc_num, details in data.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            self.accounts = {}
            self.save_to_file()

    def create_account(self, name, initial_deposit):
        account_number = random.randint(100_00, 999_99)
        while account_number in self.accounts:
            account_number = random.randint(100_00, 999_99)

        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        print(f"Account created successfully! Your account number is {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
            self.save_to_file()
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
            self.save_to_file()
        else:
            print("Account not found.")

def main():
    bank = Bank()
    while True:
        print("\nWelcome to the Bank System")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print('Please, choose a number from 1 to 5')
            continue

        if choice == 1:
            name = input("Enter your name: ")
            try:
                initial_deposit = float(input("Enter initial deposit: "))
                bank.create_account(name, initial_deposit)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif choice == 2:
            try:
                account_number = int(input("Enter your account number: "))
                bank.view_account(account_number)
            except ValueError:
                print("Invalid account number. Please enter a numeric value.")
        elif choice == 3:
            try:
                account_number = int(input("Enter your account number: "))
                amount = float(input("Enter deposit amount: "))
                bank.deposit(account_number, amount)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif choice == 4:
            try:
                account_number = int(input("Enter your account number: "))
                amount = float(input("Enter withdrawal amount: "))
                bank.withdraw(account_number, amount)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif choice == 5:
            print("Thank you for using the Bank System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()