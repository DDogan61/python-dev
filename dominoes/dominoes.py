import random


def distribute_dominoes(st, sn, ph, ch):
    domino_pieces = [[0, 1],
                     [0, 2], [1, 2],
                     [0, 3], [1, 3], [2, 3],
                     [0, 4], [1, 4], [2, 4], [3, 4],
                     [0, 5], [1, 5], [2, 5], [3, 5], [4, 5],
                     [0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6]]

    doubles = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]

    random.shuffle(doubles)
    sn.append(doubles.pop())
    for db in doubles:
        if sum(db) > sum(sn[0]):
            st.append(db)
        else:
            domino_pieces.append(db)

    random.shuffle(domino_pieces)
    for i in range(6):
        ph.append(domino_pieces.pop())
        ch.append(domino_pieces.pop())

    turn = random.choice(["player", "computer"])
    if turn == "computer":
        ch.append(domino_pieces.pop())
    else:
        ph.append(domino_pieces.pop())
    st.extend(domino_pieces)
    random.shuffle(st)
    return turn


def print_domino(sn):
    if len(sn) > 6:
        print(f"{sn[0]}{sn[1]}{sn[2]}...{sn[-3]}{sn[-2]}{sn[-1]}")
    else:
        for domino in sn:
            print(domino, end="")
    print("\n")


def print_turn(st, sn, ph, ch, turn, winner):
    print("=" * 70)
    print(f"Stock size:  {len(st)}")
    print(f"Computer pieces: {len(ch)}\n")
    print_domino(sn)
    print("Your pieces:")
    for index, domino in enumerate(ph, start=1):
        print(f"{index}:{domino}")
    if winner == "continue":
        if turn == "player":
            state = "It's your turn to make a move. Enter your command."
        else:
            state = "Computer is about to make a move. Press Enter to continue..."
    elif winner == "player":
        state = "The game is over. You won!"
    elif winner == "computer":
        state = "The game is over. The computer won!"
    else:
        state = "The game is over. It's a draw!"
    print(f"\nStatus: {state}")


def add_domino(snake, stock, hand, choice):
    if choice == 0:
        if len(stock) > 0:
            hand.append(stock.pop())
    elif choice > 0:
        snake.append(hand.pop(choice - 1))
    else:
        snake.insert(0, hand.pop(abs(choice) - 1))


def swap(domino):
    temp = domino[0]
    domino[0] = domino[1]
    domino[1] = temp


def check_validity(snake, hand, choice):
    if choice == 0:
        return True
    elif choice > 0:
        end = snake[-1][1]
    else:
        end = snake[0][0]

    domino = hand[abs(choice) - 1]

    if end in domino:
        if (choice > 0 and end != domino[0]) or (choice < 0 and end != domino[1]):
            swap(domino)
        return True
    else:
        return False


def check_user_input(choice, possible_choices):
    try:
        num = int(choice)
        if num in possible_choices:
            return num
        return None
    except:
        return None


def player_input(stock, snake, player_hand):
    possible_choices = [i for i in range(len(player_hand) + 1)]
    possible_choices.extend([-i for i in range(1, len(player_hand) + 1)])
    possible_choices.sort()
    while True:
        choice = input()
        result = check_user_input(choice, possible_choices)
        if result is not None:
            choice = result
            if check_validity(snake, player_hand, choice):
                break
        print("Invalid input. Please try again.")
    add_domino(snake, stock, player_hand, choice)


def computer_ai(snake, computer_hand):
    scores = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for domino in snake:
        for num in domino:
            scores[num] += 1

    hand_scores = {}
    for index, domino in enumerate(computer_hand, start=1):
        first = domino[0]
        second = domino[1]
        hand_scores[index] = scores[first] + scores[second]

    hand_scores = dict(sorted(hand_scores.items(), key=lambda x: x[1]))

    left_edge = snake[0][0]
    right_edge = snake[-1][1]
    for key in hand_scores.keys():
        if left_edge in computer_hand[key - 1]:
            return -key
        if right_edge in computer_hand[key - 1]:
            return key
    return 0


def computer_input(stock, snake, computer_hand):
    choice = computer_ai(snake, computer_hand)
    if choice == 0:
        pass
    elif choice > 0:
        domino = computer_hand[abs(choice) - 1]
        end = snake[-1][1]
        if end != domino[0]:
            swap(domino)
    else:
        domino = computer_hand[abs(choice) - 1]
        end = snake[0][0]
        if end != domino[1]:
            swap(domino)
    add_domino(snake, stock, computer_hand, choice)


def take_input(stock, snake, player_hand, computer_hand, turn):
    if turn == "player":
        player_input(stock, snake, player_hand)
    else:
        input()
        computer_input(stock, snake, computer_hand)


def check_winning_condition(snake, player_hand, computer_hand):
    if not player_hand:
        return "player", False
    elif not computer_hand:
        return "computer", False
    else:
        if snake[0][0] == snake[-1][1]:
            edge = snake[0][0]
            count = 0
            for domino in snake:
                for num in domino:
                    if num == edge:
                        count += 1
            if count == 8:
                return "draw", False
    return "continue", True


def main():
    stock = []
    snake = []
    player_hand = []
    computer_hand = []
    turn = distribute_dominoes(stock, snake, player_hand, computer_hand)
    game_state = True
    while game_state:
        print_turn(stock, snake, player_hand, computer_hand, turn, "continue")
        take_input(stock, snake, player_hand, computer_hand, turn)
        turn = "computer" if turn == "player" else "player"
        winner, game_state = check_winning_condition(snake, player_hand, computer_hand)
    print_turn(stock, snake, player_hand, computer_hand, turn, winner)


if __name__ == "__main__":
    main()
