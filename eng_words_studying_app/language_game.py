import json
import requests
import random
import logging


logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
file_handler = logging.FileHandler(f"{'user_actions'}.log", mode='w')

formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s - %(asctime)s", datefmt="%Y-%m-%d %H:%M:%S")

handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

API_URL = "https://api.mymemory.translated.net/get"

class Translator:

    def __init__(self):
        self.api = API_URL

    def api_check(self):
        try:
            response = requests.get(self.api, timeout=3)
            print(f'api доступен')
        except requests.Timeout:
            print("Timeout error!")
            logger.error("Timeout error!")
        except requests.ConnectionError:
            print("Connection error")
            logger.error("Connection error!")

    def get_translation(self, word):
        params = {"q": word, "langpair": "ru|en"}
        response = requests.get(self.api, params=params).json()

        translations = [match["translation"] for match in response.get("matches", []) if match["translation"]]
        return list(set(translations)) if translations else []

class LanguageGame:

    def __init__(self):
        self.translator = Translator()
        self.leader_board = LeaderBoard()
        self.leader_board.load_players()
        self.words_list = self.load_words()
        self.counter = 0
        self.tryes = 0

    def load_words(self):
        with open("words.txt", "r") as file:
            info = file.readlines()
            info = list(map(str.strip, info))

        return info

    def random_word(self, count = 3):
        random_words = ["apple", "table", "chair", "bottle", "window", "book", "computer", "car", "street", "house"]
        result = random.sample(random_words, min(count, len(random_words)))
        result = list(map(str.lower, result))
        return result

    def play(self):
        username = input("Enter your username: ")
        self.current_player = self.leader_board.add_player(username)
        while True:
            any_word = random.choice(self.words_list)
            translated_word = self.translator.get_translation(any_word)
            correct_answer = translated_word[0].lower()
            mix_answers = self.random_word() + [correct_answer]
            random.shuffle(mix_answers)
            print(f"Ваше слово '{any_word}', выберите правильный вариант: {mix_answers}")
            try:
                user_choice = input("Введите ваш выбор: ")
                if user_choice == correct_answer:
                    self.counter += 1
                    print("Ответ верный!")
                else:
                    print(f"Ответ не верный! Правильный ответ - {correct_answer}")
                    self.tryes += 1
            except ValueError:
                print("Неверный ввод!")
                logger.warning("Неверный ввод!")


            self.result_counter()

    def result_counter(self):
        self.current_player.total_scores = self.counter
        self.current_player.played_games = self.tryes

        if self.counter == 5 or self.tryes == 3:
            print("Игра окончена")
            self.leader_board.save_players()
            exit(0)

    def stat(self):
        try:
            with open(r"stat.json", "w") as file:
                json.dump(self.counter, file, indent=4)
                json.dump(self.tryes, file, indent=4)
                logger.info("Информация сохранена")
        except IOError as e:
            logger.error(f"Failed to save data: {e}")

class Player:
    def __init__(self, username, total_scores, played_games):
        self.username = username
        self.total_scores = total_scores
        self.played_games = played_games

class LeaderBoard:
    players = {}
    def save_players(self):
        with open("players.json", "w") as file:
            info = {}
            for username, player in self.players.items():
                info[username] = {
                    "username": player.username,
                    "total_scores": player.total_scores,
                    "played_games": player.played_games
                }
            json.dump(info, file, indent=2)
            logger.info("Пользователи сохранены!")

    def load_players(self):
        with open("players.json", "r") as file:
            info = json.load(file)
            for username, player in info.items():
                self.players[username] = Player(**player)

            logger.info("Список пользователей загружен!")

    def add_player(self, username):
        if username in self.players:
            logger.warning("Такой пользователь уже существует!")

        else:
            self.players[username] = Player(username, 0, 0)
            self.save_players()

        return self.players[username]

    def show_leader_board(self):
        print("Username - Total scores - Played games")
        for username, player in self.players.items():
            print(username, player.total_scores, player.played_games)

    def clear_leader_board(self):
        saver = input("Are you sure?(Y/N): ").lower()
        if saver == "y":
            self.players = {}
            print("Leaderboard was cleared!")
            logger.info("Leaderboard was cleared!")
        else:
            return

def main():
    game = LanguageGame()

    while True:
        try:
            user_input = input(
                "1.New game\n"
                "2.Check results\n"
                "3.Clear leaderboard\n"
                "4.Exit game\n"
                "Your choice(1-3): "
            )

            match user_input:
                case "1":
                    game.play()
                case "2":
                    game.leader_board.show_leader_board()
                case "3":
                    game.leader_board.clear_leader_board()
                case "4":
                    exit(0)


        except Exception as e:
            print(f"Ошибка: {e}")
            logger.error(f"Ошибка: {e}")
        except KeyboardInterrupt:
            print("Пока пока!")
            logger.info("Пользователь отменил ввод")
            break

if __name__ == '__main__':
    main()
