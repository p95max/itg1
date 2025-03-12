class BankUser:
    def __init__(self, user_name, user_age, user_address):
        self.user_name = user_name
        self.user_age = user_age
        self.user_address = user_address

    def welcome_user(self):
        print(f"Greetings '{self.user_name}'")
        print("-----------------------------")

class BankAccount:
    def __init__(self):
        self.user_accounts = {}

    def open_new_account(self, acc_name):
        if acc_name in self.user_accounts:
            print(f"Account {acc_name} is already exist!")
        else:
            self.user_accounts[acc_name] = {"Total balance": 0}
        print(f"User created new account '{acc_name}'")

    def show_accounts(self):
        if not self.user_accounts:
            print("No opened accounts")
        else:
            for acc_name, details in self.user_accounts.items():
                print(f"Account: {acc_name}, Balance: {details['Total balance']}$")

    def add_funds(self, acc_name, amount: int):
        if acc_name not in self.user_accounts:
            print("Account not exist!")
            return
        if amount > 0:
            self.user_accounts[acc_name]["Total balance"] += amount
            print(f"Your account '{acc_name}' top up to {amount}, current balance:{self.user_accounts[acc_name]["Total balance"]}")

    def withdraw_funds(self, acc_name, amount: int):
        if acc_name not in self.user_accounts:
            print("Account does not exist!")
            return
        if self.user_accounts[acc_name]["Total balance"] >= amount > 0:
            self.user_accounts[acc_name]["Total balance"] -= amount
            print(f"Withdraw {amount} from '{acc_name}'. Current balance: {self.user_accounts[acc_name]['Total balance']}")
        else:
            print("Not enough funds or invalid amount!")

    def remove_account(self, acc_name):
        if acc_name not in self.user_accounts:
            print("Account does not exist!")
            return
        if self.user_accounts[acc_name]["Total balance"] > 0:
            print("Warning! You have funds on the account! Please withdraw or transfer it.")
            return
        del self.user_accounts[acc_name]
        print(f"Account '{acc_name}' was deleted!")

user = BankUser("Max", 30, "Chemnitz")
user.welcome_user()
banking = BankAccount()


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
            banking.show_accounts()
        case "2":
            acc_name = input("Enter account name: ")
            acc_name = acc_name.lower()
            banking.open_new_account(acc_name)
        case "3":
            amount = int(input("Enter Account name and sum for top up account: "))
            banking.add_funds(acc_name, amount)
        case "4":
            amount = int(input("Enter Account name and sum for top up account: "))
            banking.withdraw_funds(acc_name, amount)
        case "5":
            acc_name = input("Enter account name for deleting: ")
            banking.remove_account(acc_name)
        case "6":
            print("Exiting program")
            break

        case _:
            print("Invalid option, please try again.")