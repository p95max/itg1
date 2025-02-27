import json
from datetime import datetime

class QuizGame:
    questions = {
        "Столица Франции?": ["1. Лондон", "2. Берлин", "3. Париж"],
        "Столица Германии?": ["1. Лондон", "2. Берлин", "3. Венеция"],
        "Столица США?": ["1. Нью-Йорк", "2. Лос-Анджелес", "3. Вашингтон"],
        "Столица Греции?": ["1. Афины", "2. Стамбул", "3. Киев"],
        "Столица Норвегии?": ["1. Осло", "2. Порту", "3. Мюнхен"]
    }
    correct_answers = {
        "Столица Франции?": "3",
        "Столица Германии?": "2",
        "Столица США?": "3",
        "Столица Греции?": "1",
        "Столица Норвегии?": "1"
    }

    users_results_file = "user_results.json"

    def __init__(self):
        self.scores = 0
        self.questions_list = list(QuizGame.questions.items())
        self.quiz_start = None
        self.end_time = None
        self.username = None
        self.users_results = []

    def start_game(self):
        print("Добро пожаловать в Квиз!")
        self.quiz_start = datetime.now()

    def user_registration(self):
        self.username = input("Введите ваше Имя и фамилию через пробел: ")
        while len(self.username.split()) < 2:
            self.username = input("Введите корректно (Имя и Фамилия через пробел): ").strip()

    def show_question_and_answer(self):
        for question, answers in self.questions_list:
            print(question)
            for answer in answers:
                print(answer)
            while True:
                enter_ans = input("Введите номер ответа (1-3): ")
                try:
                    enter_ans = int(enter_ans)
                    if enter_ans not in range(1, 4):
                        print("Ошибка ввода! Выберите 1-3!")
                    else:
                        break
                except ValueError:
                    print("Введите номер вопроса 1-3!")

            self.check_answer(str(enter_ans), question)
        self.end_time = datetime.now()

    def check_answer(self, enter_ans, question):
        is_correct = enter_ans == QuizGame.correct_answers[question]
        if is_correct:
            print("Ответ верный!")
            self.scores += 1
        else:
            print("Ответ неверный!")

        self.users_results.append({
            "question": question,
            "user_answer": enter_ans,
            "correct_answer": QuizGame.correct_answers[question],
            "is_correct": is_correct
        })

    def result_save(self):
        def load_results():
            try:
                with open(QuizGame.users_results_file, "r") as file:
                    return json.load(file)
            except FileNotFoundError:
                return []

        def save_results(results):
            with open(QuizGame.users_results_file, "w") as file:
                json.dump(results, file, indent=4, ensure_ascii=False)

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

        total_questions = len(self.questions_list)
        self.result_percent = (self.scores / total_questions) * 100

        final_result = {
            "username": self.username,
            "start_time": self.quiz_start.strftime("%Y-%m-%d %H:%M"),
            "end_time": self.end_time.strftime("%Y-%m-%d %H:%M"),
            "total_questions": total_questions,
            "correct_answers": self.scores,
            "result_percent": self.result_percent,
            "details": self.users_results
        }

        all_results = load_results()
        all_results.append(final_result)
        save_results(all_results)

        txt_filename = f"result_{self.username.replace(' ', '_')}.txt"
        save_to_txt(txt_filename, final_result)

    def show_results(self):
        print(f"Пользователь '{self.username}' имеет: {self.scores} правильных ответов из {len(self.questions_list)}")
        print(f"Правильных ответов пользователя'{self.username}' - {self.result_percent}%")


game = QuizGame()
game.start_game()
game.user_registration()
game.show_question_and_answer()
game.result_save()
game.show_results()