import json
import logging


def install_logging():
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    file_handler = logging.FileHandler(f"{"user_actions"}.log", mode='w')

    formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")

    handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)

    return logger

class UserRegistration:
    """Feature for new user registration"""
    users = {}
    def __init__(self, logger):
        self.logger = logger
        self.name = None
        self.password = None
        self.age = None


        self.load_from_file()

    def register_for_main_menu(self):
        """Method for registration in main menu"""
        self.valid_username()
        self.valid_userage()
        self.valid_userpass()

    def valid_username(self):
        """Username validation"""
        while True:
            self.name = input("Enter your name:\nName: ")
            self.name = self.name.lower()
            if self.name in UserRegistration.users:
                self.logger.warning(f"Name {self.name} is already taken! Choose another!")
            else:
                break

    def valid_userage(self):
        """User age validation"""
        while True:
            try:
                self.age = int(input("Enter your age:\nYour age: "))
                if self.age >= 18:
                    break
                else:
                    self.logger.warning("You are too young!")
            except ValueError:
                self.logger.error("Error! Use only numbers!")

    def valid_userpass(self):
        """User password validation"""
        while True:

            user_pass = input("Enter your password\n(min. 4 symbols): ")
            if len(user_pass) < 4:
                self.logger.warning("Your password is too short! Minimum 4 symbols!")
                continue

            check_user_pass = input("\nEnter your password again: ")
            if user_pass == check_user_pass:
                self.password = user_pass
                self.save_user_data()
                self.save_in_file()
                break
            else:
                self.logger.warning("Passwords not match! Try again!")

    def save_user_data(self):
        """Save user data in dict"""
        UserRegistration.users[self.name] = {
                 "Password": self.password,
                 "Age": self.age
             }

    def save_in_file(self):
        try:
            with open("users.json", "w") as file:
                json.dump(UserRegistration.users, file, indent=4)
                self.logger.info("Data saved successfully!")
        except IOError as e:
            self.logger.error(f"Failed to save data: {e}")

    def load_from_file(self):
        """Load user data from file"""
        try:
            with open("users.json", "r") as file:
                UserRegistration.users = json.load(file)
                self.logger.info("Data load successfully!")

        except (FileNotFoundError, json.JSONDecodeError):
            self.logger.warning("No previous user data was found")

    def show_user_list(self):
        """Show current users from dict/file"""
        return f"Current users:\n{UserRegistration.users}"

    def clear_users(self):
        saver = input("Are you sure? All data will be deleted!\n(Print 'Y'/'N'): ")
        saver = saver.lower()
        if saver == "y":
            UserRegistration.users = {}
            try:
                self.save_in_file()  # Сначала сохраняем
                self.logger.warning("Database is cleared!")
            except IOError as e:
                self.logger.error(f"Failed to clear database: {e}")
        else:
            self.logger.info("Returning to main menu")
            return

class UserAuthorisation():
    """Feature for user authorisation"""

    def __init__(self, logger):
        self.logger = logger
        self.current_user = None

    def authoris_for_main_menu(self):
        """Method for user authorisation for main menu"""
        self.valid_username()
        self.valid_userpass()

    def valid_username(self):
        """Username validation before authorisation"""
        while True:
            self.current_user = input("Enter your name: ")
            self.current_user = self.current_user.lower()
            if self.current_user in UserRegistration.users:
                self.logger.info(f"User '{self.current_user}' found!")
                break
            else:
                self.logger.warning(f"User '{self.current_user}' not found!")
                return

    def valid_userpass(self):
        """User password validation"""
        while True:

            user_pass = input("Enter pass (min. 4 symbols): ")
            if len(user_pass) < 4:
                self.logger.warning("Your password is too short! Minimum 4 symbols!")
                continue
            if user_pass == UserRegistration.users[self.current_user]['Password']:
                self.logger.info(f"Correct password '{self.current_user}', access granted!")
                return True
            else:
                self.logger.warning("Wrong pass!")


def main():
    """Contains main menu"""
    logger = install_logging()
    user_reg = UserRegistration(logger)
    user_auth = UserAuthorisation(logger)

    while True:
        try:
            user_input = input(
                "1. Show all users.\n"
                "2. User registration.\n"
                "3. User authorisation.\n"
                "4. Clear all users.\n"
                "5. Exit.\n"
                "Your choise(1-5): "
            )

            match user_input:
                case "1":
                    logger.info(user_reg.show_user_list())
                case "2":
                    user_reg.register_for_main_menu()
                case "3":
                    user_auth.authoris_for_main_menu()
                case "4":
                    user_reg.clear_users()
                case "5":
                    logger.info("Exiting program")
                    break
                case _:
                    logger.info("Invalid option, please try again.")

        except Exception as e:
            logger.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()


