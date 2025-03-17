import json
import os
import logging

def install_logging():
    logger = logging.getLogger("user_actions")
    handler = logging.StreamHandler()
    file_handler = logging.FileHandler(f"{"user_actions"}.log", mode='w')

    formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s - %(asctime)s", datefmt="%Y-%m-%d %H:%M:%S")

    file_handler.setFormatter(formatter)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)

    return logger

class BankUser:
    user_accounts = {}

    def __init__(self, logger):
        self.banking_data = "banking_data.json"
        self.logger = logger

        self.load_data_from_file()

    def open_new_account(self, acc_name):
        if acc_name in self.user_accounts:
            self.logger.warning(f"Account {acc_name} is already exist!")
            return
        else:
            self.user_accounts[acc_name] = {"Total balance": 0}
            self.logger.info(f"User created new account '{acc_name}'")
        self.save_info()

    def remove_account(self, acc_name):
        acc_name = acc_name.lower()
        if acc_name not in self.user_accounts:
            self.logger.warning("Account does not exist!")
            return
        if self.user_accounts[acc_name]["Total balance"] > 0:
            self.logger.error("Error! You have funds on the account! Please withdraw or transfer it.")
            return
        del self.user_accounts[acc_name]
        self.logger.warning(f"Account '{acc_name}' was deleted!")
        self.save_info()

    def save_info(self):
        try:
            with open(self.banking_data, "w") as file:
                json.dump(self.user_accounts, file, indent=4)
            self.logger.info("Banking data saved successfully.")
        except IOError as e:
            self.logger.error(f"Failed to save banking data: {e}")

    def load_data_from_file(self):
        if os.path.exists(self.banking_data) and os.path.getsize(self.banking_data) > 0:
            try:
                with open(self.banking_data, "r") as file:
                    self.user_accounts = json.load(file)
                self.logger.info("Banking data loaded successfully.")
            except json.JSONDecodeError:
                self.logger.error("Error reading banking data file")
                self.user_accounts = {}
        else:
            self.logger.warning("No banking data found.")

class Banking:
    def __init__(self, logger, bank_user):
        self.current_user = None
        self.logger = logger
        self.bank_user = bank_user

    def show_accounts(self):
        if not BankUser.user_accounts:
            self.logger.info("No opened accounts")
        else:
            for acc_name, details in BankUser.user_accounts.items():
                self.logger.info(f"Account: {acc_name}, Balance: {details['Total balance']}$")

    def add_funds(self, acc_name, amount: int):
        acc_name = acc_name.lower()
        if acc_name not in BankUser.user_accounts:
            self.logger.warning("Account not exist!")
            return
        if amount > 0:
            BankUser.user_accounts[acc_name]["Total balance"] += amount
            self.logger.info(f"Your account '{acc_name}' top up to {amount}, current balance:{BankUser.user_accounts[acc_name]["Total balance"]}")
            self.bank_user.save_info()

    def withdraw_funds(self, acc_name, amount: int):
        acc_name = acc_name.lower()
        if acc_name not in BankUser.user_accounts:
            self.logger.warning("Account does not exist!")
            return

        if BankUser.user_accounts[acc_name]["Total balance"] >= amount > 0:
            BankUser.user_accounts[acc_name]["Total balance"] -= amount
            self.logger.info(f"Withdraw {amount} from '{acc_name}'. Current balance: {BankUser.user_accounts[acc_name]['Total balance']}")
            self.bank_user.save_info()

        else:
            self.logger.warning("Not enough funds or invalid amount!")

logger = install_logging()
user = BankUser(logger)
banking = Banking(logger, user)


def main():
    while True:
        try:
            user_input = input(
                "1. Show your opened accounts.\n"
                "2. Add new account.\n"
                "3. Top up funds.\n"
                "4. Withdraw funds.\n"
                "5. Delete account.\n"
                "6. Exit.\n"
                "Your choice: "
            )

            match user_input:

                case "1":
                    banking.show_accounts()
                case "2":
                    acc_name = input("Enter account name: ")
                    acc_name = acc_name.lower()
                    user.open_new_account(acc_name)
                case "3":
                    acc_name = input("Enter account name: ").lower()
                    amount = int(input("Enter amount to top up: "))
                    banking.add_funds(acc_name, amount)
                case "4":
                    acc_name = input("Enter account name: ").lower()
                    amount = int(input("Enter amount to withdraw: "))
                    banking.withdraw_funds(acc_name, amount)
                case "5":
                    acc_name = input("Enter account name for deleting: ")
                    user.remove_account(acc_name)
                case "6":
                    logger.info("Exiting program")
                    break

                case _:
                    logger.warning("Invalid option, please try again.")

        except ValueError:
            logger.error("Invalid input! Please enter a valid number.")
        except Exception as e:
            logger.error(f"An error occurred: {e}")
        except KeyboardInterrupt:
            logger.warning("User closed app!")
            break

if __name__ == '__main__':
    main()
