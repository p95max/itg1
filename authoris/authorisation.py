import json

class UserRegistration:
    users = {}
    def __init__(self):
        self.name = None
        self.password = None
        self.age = None

        self.load_from_file()
        self.valid_username_userage()
        self.valid_userpass()

    def valid_username_userage(self):
        while True:
            self.name = input("Enter your name: ")
            self.name = self.name.lower()
            if self.name in UserRegistration.users:
                print("Name is already taken! Choose another!")
            else:
                break

        while True:
            try:
                self.age = int(input("Enter your age: "))
                if self.age >= 18:
                    break
                else:
                    print("You are too young!")
            except ValueError:
                print("Error! Use only numbers!")

    def valid_userpass(self):
        while True:
            user_pass = input("Enter pass: ")
            check_user_pass = input("Enter pass again: ")
            if user_pass == check_user_pass:
                self.password = user_pass
                self.save_user_data()
                self.save_in_file()
                break
            else:
                print("Passwords not match! Try again!")

    def save_user_data(self):
        UserRegistration.users[self.name] = {
                 "Password": self.password,
                 "Age": self.age
             }

    def save_in_file(self):
        try:
            with open("users.json", "r") as file:
                existing_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = {}

        existing_data.update(UserRegistration.users)

        with open("users.json", "w") as file:
            json.dump(existing_data, file, indent=4)
            print("Data saved successfully!")

    def load_from_file(self):
        try:
            with open("users.json", "r") as file:
                UserRegistration.users = json.load(file)
                print("Data load successfully!")

        except (FileNotFoundError, json.JSONDecodeError):
            print("No previous user data was found")

    def show_user_list(self):
        return UserRegistration.users

    def clear_users(self):
        UserRegistration.users = {}


def main():

    registration = UserRegistration()
    print("Saved users:\n", registration.show_user_list())
    # registration.clear_users()

if __name__ == '__main__':
    main()
