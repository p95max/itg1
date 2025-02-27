import json
from datetime import datetime

#Работа с файлами
def question_load(file_path):
    try:

        with open(file_path, "r") as file:
            questions = json.load(file)
            return questions["questions"]

    except FileNotFoundError:
        print("Файл с ответами не найден!")
        return None

def load_results(users_results_file):
    try:
        with open(users_results_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Файл с результатами не найден!")
        return None

def save_results(users_results_file, results):
    with open(users_results_file, "w") as file:
        json.dump(results, file, indent=8, ensure_ascii=False)

def save_to_txt(filename, final_result):
    with open(filename, "w") as file:
        file.write(f"Имя и фамилия: {final_result['username']}\n")
        file.write(f"Время начала теста: {final_result['start_time']}\n")
        file.write(f"Время окончания теста: {final_result['end_time']}\n")
        file.write(f"Всего вопросов: {final_result['total_questions']}\n")
        file.write(f"Правильных ответов: {final_result['correct_answers']}\n")
        file.write(f"Результат: {final_result['result_percent']:.2f}%\n\n")
        file.write("Детали теста:\n")
        for item in final_result["details"]:
            file.write(f"Вопрос: {item['question']}\n")
            file.write(f"Ваш ответ: {item['user_answer']}\n")
            file.write(f"Правильный ответ: {item['correct_answer']}\n")
            file.write(f"Правильно: {item['is_correct']}\n")
            file.write("-" * 30 + "\n")


#Ссылки на файлы
file_path = "questions_for_quiz.json"
users_results_file = "user_results.json"
questions = question_load(file_path)

#Авторизация
username = input("Введите ваше Имя и фамилию через пробел: ")
while len(username.split()) < 2:
    username = input("Введите корректно (Имя и Фамилия через пробел): ").strip()

#Запуск таймера
quiz_start = datetime.now()

correct_answers = {
    "Столица Франции?": "3",
    "Столица Германии?": "2",
    "Столица США?": "3",
    "Столица Греции?": "1",
    "Столица Норвегии?": "1"
}

#Основная логика
scores = 0
total_questions = len(questions)
users_results = []

for question, answers in questions.items():
    print(f"\n{question}")
    for answer in answers:
        print(answer)

    enter_ans = input("Введите номер ответа (1-3): ").strip()

    if enter_ans == correct_answers[question]:
        print("Ответ верный!")
        scores += 1
    else:
        print("Ответ неверный!")

    users_results.append({
        "question": question,
        "user_answer": enter_ans,
        "correct_answer": correct_answers[question],
        "is_correct": enter_ans == correct_answers[question]
    })

#Конец таймера
end_time = datetime.now()

#Обработка результата
result_persent = (scores / total_questions) * 100

final_result = {
    "username": username,
    "start_time": quiz_start.strftime("%Y-%m-%d %H:%M:%S"),
    "end_time": end_time.strftime("%Y-%m-%d %H:%M:%S"),
    "total_questions": total_questions,
    "correct_answers": scores,
    "result_percent": result_persent,
    "details": users_results
}

all_results = load_results(users_results_file)
all_results.append(final_result)
save_results(users_results_file, users_results)

txt_filename = f"result_{username.replace(' ', '_')}.txt"
save_to_txt(txt_filename, final_result)

print(f"Ваш итоговый счет: {scores} верных ответов из {len(questions)}")
print(f"Ваш результат в %: {result_persent}%")
print(f"Результаты сохранены в файл: {txt_filename}")