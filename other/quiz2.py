# Quiz

# Question_list

switcher = {
    "What capital of the Great Britain?": "London",
    "Who is a current US President?": "Trump",
    "Which country has the biggest population?": "India"
}

scores = 0
correct_ans = "Correct "
wrong_ans = "Wrong!"

for question, correct_ans in switcher.items():
    print(question)
    enter_ans = str(input())

    if enter_ans == correct_ans:
        print(correct_ans)
        scores += 1
    else:
        print(wrong_ans)
        scores + 1


print("Your correct answers: " + str(scores))
