
def registration():
    users = {}

    username = input("Enter your name: ")
    if username in users:
        print("Choose another name!")

    userpass = input("Enter password: ")

    users[username] = {"Password:": userpass}

    return users

print(registration())


