#Score_counter
#1win=3, 1ties=1

print("Enter your scores")
wins = int(input())
ties = int(input())

score = (wins * 3) + (ties * 1)  

message = "Your Score: " + str(score)
print(message)