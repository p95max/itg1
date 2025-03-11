class BankUser:
    def __init__(self):
        self.user_name = None
        self.user_balance = 0
        self.user_accounts = {}

    def user_autorisation(self):
        self.user_name = input("Enter your username: ")
        print(f"User {self.user_name} is authorised!")

    def open_new_account(self, acc_name):
        if self.user_name not in self.user_accounts:
            self.user_accounts[self.user_name] = []

        self.user_accounts[self.user_name].append({
            "Account name": acc_name,
            "Total balance": self.user_balance
        })

        print(f"User '{self.user_name}' created new account '{acc_name}'")

    def show_accounts(self):
        if not self.user_accounts:
            print("No opened accounts")
        else:
            print(self.user_accounts[self.user_name])


# class BankAccount:
#     def __init__(self):
#         self.


user = BankUser()
user.user_autorisation()


while True:
    user_input = input(
        "1. Show your accounts.\n"
        "2. Add new account.\n"
        "3. Delete task.\n"
        "4. Change task status.\n"
        "5. Clear tasks list.\n"
        "6. Exit.\n"
    )

    match user_input:

        case "1":
            user.show_accounts()
        case "2":
            acc_name = input("Enter account name: ")
            acc_name = acc_name.lower()
            user.open_new_account(acc_name)
        # case "3":
        #     task_name = input("Enter task name for deleting: ")
        #     mananger.remove_task(task_name)
        # case "4":
        #     task_name = input("Enter task name for status changing: ")
        #     new_status = input("Enter new status(done/not done): ")
        #     mananger.change_task_status(task_name, new_status == "done")
        # case "5":
        #     mananger.clear_tasks()
        case "6":
            print("Exiting program")
            break

        case _:
            print("Invalid option, please try again.")