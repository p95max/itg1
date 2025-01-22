#e_locker

import time

correct_pass = 22222
max_attempts = 3
attempts = 0

runProgram = True
while runProgram == True:

     while attempts < max_attempts:
        try:
            enter = "Enter password: "
            print(enter)
            enter_pass = int(input())

            denied = "ACCESS DENIED!"
            granted = "ACCESS GRANTED"

            if enter_pass == correct_pass:
                print(granted)
                attempts = 0
                runProgram = False
                break

            else:
                print(denied)
            attempts += 1


        except ValueError:
            print("Error! Please enter a number.")

     if attempts == max_attempts:
       print("Locker is blocked!(5s)")
     if runProgram == True:
       time.sleep(5)
       attempts = 0