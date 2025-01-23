# Quiz

#Question_list

question1 = "What capital of the Great Britain?"
answer1a = "London"

question2 = "Who is a current US President?"
answer2a = "Trump"

question3 = "Which country has the biggest population?"
answer3a = "India"

scores = 0
correct_ans = "Correct "
wrong_ans = "Wrong!"

if answer1a and answer2a and answer3a == correct_ans:
    scores + 1

#Q1

print(question1)
enter_ans = str(input())

if enter_ans == answer1a:
    print(correct_ans)
    scores += 1
else:
    print(wrong_ans)
    scores + 1
    
#Q2

print(question2)
enter_ans = str(input())

if enter_ans == answer2a:
    print(correct_ans)
    scores += 1
else:
    print(wrong_ans)
    scores + 1
    
#Q3

print(question3)
enter_ans = str(input())

if enter_ans == answer3a:
    print(correct_ans)
    scores += 1
else:
    print(wrong_ans)
    scores + 1

print("Your correct answers: " + str(scores))
