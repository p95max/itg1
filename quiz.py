# Quiz

#Question_list

question1 = "What capital of the Great Britain?"
answer1 = "London"

question2 = "Who is a current US President?"
answer2 = "Trump"

question3 = "Which country has the biggest population?"
answer3 = "India"

scores = 0
correct_ans = "Correct "
wrong_ans = "Wrong!"

if answer1 and answer2 and answer3 == correct_ans:
    scores + 1

#Q1

print(question1)
enter_ans = str(input())

if enter_ans == answer1:
    print(correct_ans)
    scores + 1
else:
    print(wrong_ans)
    scores += 1
    
#Q2

print(question2)
enter_ans = str(input())

if enter_ans == answer2:
    print(correct_ans)
    scores + 1
else:
    print(wrong_ans)
    scores += 1
    
#Q3

print(question3)
enter_ans = str(input())

if enter_ans == answer3:
    print(correct_ans)
    scores + 1
else:
    print(wrong_ans)
    scores += 1

print("Your correct answers: " + str(scores))
