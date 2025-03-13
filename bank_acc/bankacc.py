import json
import os

class BankUser:
    def __init__(self, user_name, user_age, user_address):
        self.user_name = user_name
        self.user_age = user_age
        self.user_address = user_address
        self.banking = Banking(self.user_name)

    def welcome_user(self):
        print(f"Greetings '{self.user_name}'")
        print("-----------------------------")

class Banking:
    def __init__(self, user_name):
        self.user_name = user_name
        self.banking_data = f"{self.user_name}_banking_data.json"
        self.user_accounts = {}
        self.load_data_from_file()

    def open_new_account(self, acc_name):
        acc_name = acc_name.lower()
        if acc_name in self.user_accounts:
            print(f"Account {acc_name} is already exist!")
        else:
            self.user_accounts[acc_name] = {"Total balance": 0}
        print(f"User created new account '{acc_name}'")
        self.save_info()

    def show_accounts(self):
        if not self.user_accounts:
            print("No opened accounts")
        else:
            for acc_name, details in self.user_accounts.items():
                print(f"Account: {acc_name}, Balance: {details['Total balance']}$")

    def add_funds(self, acc_name, amount: int):
        acc_name = acc_name.lower()
        if acc_name not in self.user_accounts:
            print("Account not exist!")
            return
        if amount > 0:
            self.user_accounts[acc_name]["Total balance"] += amount
            print(f"Your account '{acc_name}' top up to {amount}, current balance:{self.user_accounts[acc_name]["Total balance"]}")
            self.save_info()

    def withdraw_funds(self, acc_name, amount: int):
        acc_name = acc_name.lower()
        if acc_name not in self.user_accounts:
            print("Account does not exist!")
            return
        if self.user_accounts[acc_name]["Total balance"] >= amount > 0:
            self.user_accounts[acc_name]["Total balance"] -= amount
            print(f"Withdraw {amount} from '{acc_name}'. Current balance: {self.user_accounts[acc_name]['Total balance']}")
            self.save_info()
        else:
            print("Not enough funds or invalid amount!")

    def remove_account(self, acc_name):
        acc_name = acc_name.lower()
        if acc_name not in self.user_accounts:
            print("Account does not exist!")
            return
        if self.user_accounts[acc_name]["Total balance"] > 0:
            print("Error! You have funds on the account! Please withdraw or transfer it.")
            return
        del self.user_accounts[acc_name]
        print(f"Account '{acc_name}' was deleted!")
        self.save_info()

    def save_info(self):
        with open(self.banking_data, "w") as file:
            json.dump(self.user_accounts, file, indent=4)
        print("Banking data saved successfully.")

    def load_data_from_file(self):
        if os.path.exists(self.banking_data) and os.path.getsize(self.banking_data) > 0:
            try:
                with open(self.banking_data, "r") as file:
                    self.user_accounts = json.load(file)
                print("Banking data loaded successfully.")
            except json.JSONDecodeError:
                print("Error reading banking data file, starting fresh.")
                self.user_accounts = {}
        else:
            print("No banking data found.")


user = BankUser("Max", 30, "Chemnitz")
user.welcome_user()

while True:
    user_input = input(
        "1. Show your opened accounts.\n"
        "2. Add new account.\n"
        "3. Top up funds.\n"
        "4. Withdraw funds.\n"
        "5. Delete account.\n"
        "6. Exit.\n"
    )

    match user_input:

        case "1":
            user.banking.show_accounts()
        case "2":
            acc_name = input("Enter account name: ")
            acc_name = acc_name.lower()
            user.banking.open_new_account(acc_name)
        case "3":
            acc_name = input("Enter Account name and sum for top up from account: ")
            amount = int(input("Enter Account name and sum for top up account: "))
            user.banking.add_funds(acc_name, amount)
        case "4":
            acc_name = input("Enter Account name and sum for withdraw from account: ")
            amount = int(input("Enter Account name and sum for withdraw from account: "))
            user.banking.withdraw_funds(acc_name, amount)
        case "5":
            acc_name = input("Enter account name for deleting: ")
            user.banking.remove_account(acc_name)
        case "6":
            print("Exiting program")
            break

        case _:
            print("Invalid option, please try again.")