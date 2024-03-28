import random
yaico = False
turn_count = 0

# Функция для создания колоды карт
def create_deck():
    ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Черви', 'Буби', 'Крести', 'Пики']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck


# Функция для раздачи карт игрокам
def deal_cards(deck, num_players):
    hands = [[] for _ in range(num_players)]
    for _ in range(4):
        for i in range(num_players):
            hands[i].append(deck.pop())
    return hands, deck


# Функция для вывода карты
def card_to_str(card):
    return f"{card['rank']}  {card['suit']}"


# Создание и замешивание козыря
def trump_card(deck):
    print("--------КОЗЫРЬ:", deck[0]['suit'])
    a = deck[0]
    b = random.randint(1, len(deck)-1)
    deck[0] = deck[b]
    deck[b] = a


# Отображение руки
def display_hand(hand):
    print("Your hand:")
    for i, card in enumerate(hand, start=1):
        print(f"{i}. {card_to_str(card)}")


# Отображение стола
def display_table(cards_on_table):
    print("\nCards on the table:")
    for card in cards_on_table:
        print(f"  {card_to_str(card)}")

# Ход игрока
def player_turn(hands, num_players):
    global yaico, turn_count
    turn_count += 1
    cards_on_table = []
    for i, hand in enumerate(hands):
        print(f"\nPlayer {i + 1}'s turn:")
        display_hand(hand)
        end_turn = False

        while len(cards_on_table) <= num_players*4 and end_turn == False:
            print("Проверка на яйцо")
            if turn_count == 1:
                num_cards_to_play = min(int(input("сколько карт вы хотите сыграть (1-3)? ")), len(hand))
                if hand[0]['suit'] == hand[1]['suit'] == hand[2]['suit'] == hand[3]['suit']:
                    print('Яйцо у игрока №', i+1)
                    yaico = True
                else:
                    print("нету")
            else:

                num_cards_to_play = min(int(input("сколько карт вы хотите сыграть (1-4)? ")), len(hand))

            for _ in range(num_cards_to_play):
                display_hand(hand)
                choice = int(input("Choose a card to play (enter the number): "))
                # Проверяем, чтобы выбор был в пределах допустимых значений
                if 1 <= choice <= len(hand):
                    cards_on_table.append(hand.pop(choice - 1))
                else:
                    print("Invalid choice. Please choose a valid card.")

            display_table(cards_on_table)
            end_turn = True


def main():
    num_players = int(input("Сколько игроков?"))
    deck = create_deck()
    hands, remaining_deck = deal_cards(deck, num_players)

    print("\nRemaining cards in the deck:")
    for card in remaining_deck:
        print(f"  {card_to_str(card)}")
    trump_card(deck)

    player_turn(hands, num_players)


if __name__ == "__main__":
    main()
