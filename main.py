import os

WIN_SCORE = 3

RULES = {
    "камень": "ножницы",
    "ножницы": "бумага",
    "бумага": "камень"
}


class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""

    def choose_move(self):
        while True:
            move = input(
                f"{self.name}, выбери (камень, ножницы, бумага): "
            ).lower()

            if move in RULES:
                self.choice = move
                return

            print("Некорректный ввод. Попробуйте еще раз.")

    def add_score(self):
        self.points += 1

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")


class RockPaperScissors:
    def __init__(self):
        self.first_player = Player("Игрок 1")
        self.second_player = Player("Игрок 2")

    def determine_winner(self):
        first = self.first_player.choice
        second = self.second_player.choice

        if first == second:
            return None

        if RULES[first] == second:
            return self.first_player

        return self.second_player

    def print_score(self):
        print("\nТекущий счет:")
        print(
            f"{self.first_player.name}: {self.first_player.points} | "
            f"{self.second_player.name}: {self.second_player.points}"
        )

    def play_round(self):
        self.first_player.choose_move()

        input("\nПередайте компьютер второму игроку и нажмите Enter...")

        print("\n" * 50)

        self.second_player.choose_move()

        winner = self.determine_winner()

        print("\nРезультаты раунда:")
        print(f"{self.first_player.name}: {self.first_player.choice}")
        print(f"{self.second_player.name}: {self.second_player.choice}")

        if winner is None:
            print("Ничья!")
        else:
            winner.add_score()
            print(f"Победитель раунда: {winner.name}")

        self.print_score()

    def show_winner(self):
        print("\nИгра окончена!")

        if self.first_player.points == WIN_SCORE:
            print(f"Победил {self.first_player.name}")
        else:
            print(f"Победил {self.second_player.name}")

    def start_game(self):
        print("КАМЕНЬ - НОЖНИЦЫ - БУМАГА")
        print(f"Побеждает тот, кто первым наберет {WIN_SCORE} очка.\n")

        round_number = 1

        while (
            self.first_player.points < WIN_SCORE
            and self.second_player.points < WIN_SCORE
        ):
            print(f"\nРаунд {round_number}")
            self.play_round()
            round_number += 1

        self.show_winner()


if __name__ == "__main__":
    game = RockPaperScissors()
    game.start_game()