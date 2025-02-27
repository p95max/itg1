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

    def __init__(self):
        self.scores = 0
        self.questions_list = list(QuizGame.questions.items())

    def start_game(self):
        print("Добро пожаловать в Квиз!")

    def show_question_and_answer(self):
        for question, answers in self.questions_list:
            print(question)
            for answer in answers:
                print(answer)
            while True:
                enter_ans = input("Введите номер ответа (1-3): ")
                try:
                    enter_ans = int(enter_ans)
                    if enter_ans not in range(1,4):
                        print("Ошибка ввода! Выберите 1-3!")
                    else:
                        break
                except ValueError:
                    print("Введите номер вопроса 1-3!")

            self.check_answer(str(enter_ans), question)

    def check_answer(self, enter_ans, question):
            if enter_ans == QuizGame.correct_answers[question]:
                print("Ответ верный!")
                self.scores += 1
            else:
                print("Ответ неверный!")

    def show_results(self):
        print(f"Ваши правильные ответы: {self.scores} из {len(self.questions_list)}")

game = QuizGame()
game.start_game()
game.show_question_and_answer()
game.show_results()