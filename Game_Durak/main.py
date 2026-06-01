import random


class User:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def throw_card(self):
        while True:
            card = input(f'{self.name}, выберите карту или "lose": ')
            if card == "lose":
                return "lose"
            if card in self.hand:
                self.hand.remove(card)
                return card
            print("Такой карты нет в руке!")


class Deck:
    def __init__(self):
        suits = ['heart', 'spades', 'diamonds', 'clubs']
        values = ['09', '10', '11', '12', '13', '14']

        self.deck = [f"{v}_{s}" for v in values for s in suits]

    def give_card(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card

    def size(self):
        return len(self.deck)


class Rules:
    def __init__(self, trump):
        self.trump = trump

    def check(self, attack, defend):
        att_val, att_suit = attack.split('_')
        def_val, def_suit = defend.split('_')

        att_val = int(att_val)
        def_val = int(def_val)

        # козырь или та же масть
        if def_suit == att_suit or def_suit == self.trump:
            if def_suit == self.trump and att_suit != self.trump:
                return True

            if def_val > att_val:
                return True

        print("Нельзя отбиться этой картой!")
        return False


class Game(Rules):
    def __init__(self):
        trump = random.choice(['heart', 'spades', 'diamonds', 'clubs'])
        super().__init__(trump)
        print(f"Козырь игры: {self.trump}")

    def play(self):
        deck = Deck()

        name1 = input("Игрок 1: ")
        name2 = input("Игрок 2: ")

        hand1 = [deck.give_card() for _ in range(6)]
        hand2 = [deck.give_card() for _ in range(6)]

        p1 = User(name1, hand1)
        p2 = User(name2, hand2)

        attacker, defender = p1, p2

        while deck.size() > 0 and (p1.hand and p2.hand):

            # добор
            for player in [attacker, defender]:
                while len(player.hand) < 6 and deck.size() > 0:
                    player.hand.append(deck.give_card())

            table = []

            print(f"\nХод: атакует {attacker.name}")
            print("Рука:", attacker.hand)

            attack = attacker.throw_card()
            while attack == "lose":
                print("Атакующий не может забрать карты")
                attack = attacker.throw_card()

            table.append(attack)

            print(f"\n{defender.name} отбивается от {attack}")
            print("Рука:", defender.hand)

            while True:
                defend = defender.throw_card()

                if defend == "lose":
                    defender.hand.extend(table)
                    print("Карты забраны со стола")
                    break

                if self.check(attack, defend):
                    table.append(defend)
                    print("Отбито!")

                    attacker, defender = defender, attacker
                    break

        winner = p1 if len(p2.hand) == 0 else p2
        print(f"\nИгра окончена! Победил {winner.name}")


game = Game()
game.play()
