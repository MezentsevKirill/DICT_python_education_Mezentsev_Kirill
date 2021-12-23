
import random


def start_pieces():
    for k in range(7):
        if player_pieces[k][0] == player_pieces[k][1]:
            snake.append(player_pieces[k])
        if computer_pieces[k][0] == computer_pieces[k][1]:
            snake.append(computer_pieces[k])
    n = 6
    while [n, n] not in snake:
        n -= 1
    snake.clear()
    snake.append([n, n])


def start_status_check():
    global counter
    counter = 0
    for elem in snake:
        if elem not in player_pieces and elem not in computer_pieces:
            print("Status: It's your turn to make a move. Enter your command.")
        elif elem in computer_pieces:
            print("Status: Computer is about to make a move. Press Enter to continue...")
            computer_pieces.remove(elem)


def draw_player_pieces():
    for elem1 in snake:
        if elem1 in player_pieces:
            player_pieces.remove(elem1)
    num = 0
    while num < len(player_pieces):
        num += 1
        print(str(num) + ":", player_pieces[num-1])


def check_input():
    global counter
    print("Status: It's your turn to make a move. Enter your command.")
    valid = False
    while not valid:
        user_number = int(input("Enter command:\n> "))
        if user_number > 0:
            try:
                if snake[-1][1] in player_pieces[user_number - 1]:
                    if snake[-1][1] == player_pieces[user_number - 1][0]:
                        snake.append(player_pieces[user_number - 1])
                        player_pieces.remove(player_pieces[user_number - 1])
                        valid = True
                    else:
                        snake.append(list(reversed(player_pieces[user_number - 1])))
                        player_pieces.remove(player_pieces[user_number - 1])
                        valid = True
                else:
                    print("Illegal move.Please try again.")
                    valid = False
            except IndexError:
                print("Invalid input. Please try again.")
                valid = False
        elif user_number < 0:
            try:
                if snake[0][0] in player_pieces[(user_number * -1) - 1]:
                    if snake[0][0] == player_pieces[(user_number * -1) - 1][1]:
                        snake.insert(0, player_pieces[(user_number * -1) - 1])
                        player_pieces.remove(player_pieces[(user_number * -1) - 1])
                        valid = True
                    else:
                        snake.insert(0, list(reversed(player_pieces[(user_number * -1) - 1])))
                        player_pieces.remove(player_pieces[(user_number * -1) - 1])
                        valid = True
                else:
                    print("Illegal move.Please try again.")
                    valid = False
            except IndexError:
                print("Invalid input. Please try again.")
                valid = False
        elif user_number == 0:
            added_piece = random.choice(game_list)
            player_pieces.append(added_piece)
            game_list.remove(added_piece)
            valid = True
        elif user_number in float:
            print("Invalid input. Please try again.")


def status_check():
    global counter
    if counter % 2 == 0:
        check_input()
        counter += 1
    else:
        print("Status: Computer is about to make a move. Press Enter to continue...")
        enter = input("Enter command:\n> ")
        valid = False
        while not valid:
            computer_number = random.randint(-len(computer_pieces), len(computer_pieces))
            if computer_number > 0:
                if snake[-1][1] in computer_pieces[computer_number - 1]:
                    if snake[-1][1] == computer_pieces[computer_number - 1][0]:
                        snake.append(computer_pieces[computer_number - 1])
                        computer_pieces.remove(computer_pieces[computer_number - 1])
                        valid = True
                    else:
                        snake.append(list(reversed(computer_pieces[computer_number - 1])))
                        computer_pieces.remove(computer_pieces[computer_number - 1])
                        valid = True
                else:
                    valid = False
            elif computer_number < 0:
                if snake[0][0] in computer_pieces[(computer_number * -1) - 1]:
                    if snake[0][0] == computer_pieces[(computer_number * -1) - 1][1]:
                        snake.insert(0, computer_pieces[(computer_number * -1) - 1])
                        computer_pieces.remove(computer_pieces[(computer_number * -1) - 1])
                        valid = True
                    else:
                        snake.insert(0, list(reversed(computer_pieces[(computer_number * -1) - 1])))
                        computer_pieces.remove(computer_pieces[(computer_number * -1) - 1])
                        valid = True
                else:
                    valid = False
            elif computer_number == 0:
                added_piece = random.choice(game_list)
                computer_pieces.append(added_piece)
                game_list.remove(added_piece)
        counter += 1


# All pieces
print("=" * 70)
game_list = []
for j in range(7):
    game_list.append([j, j])
    i = 0
    while j != i:
        game_list.append([i, j])
        i += 1
# Random choice pieces
player_pieces = random.sample(game_list, 7)
for i in player_pieces:
    game_list.remove(i)
computer_pieces = random.sample(game_list, 7)
for i in computer_pieces:
    game_list.remove(i)
snake = []


# Choice start piece
start_pieces()
start_status_check()
counter = 0
print(counter)
win = False
while not win:
    print("=" * 70)
    print(counter)
    print("Stock size:", len(game_list))
    print("Computer pieces:", len(computer_pieces))
    if len(snake) <= 6:
        print(snake)
    else:
        print(str(snake[0:3]) + "..." + str(snake[-3]), str(snake[-2]), str(snake[-1]))
    # My pieces
    print("Your pieces:")
    draw_player_pieces()
    status_check()


    def check_win():
        global win
        if len(player_pieces) == 0:
            print("Status: The game is over. You won!")
            win = True
        elif len(computer_pieces) == 0:
            print("Status: The game is over. The computer won!")
            win = True
        for elem1 in snake:
            elem1.count(snake[0][0])
            if snake[0][0] == snake[-1][-1] and elem1.count(snake[0][0]) == 8:
                print("Status: The game is over. It's a draw!")
                win = True
    check_win()
