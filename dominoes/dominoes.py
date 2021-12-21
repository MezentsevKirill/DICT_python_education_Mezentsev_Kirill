import random
print("=" * 70)
game_list = []
for j in range(7):
    game_list.append([j, j])
    i = 0
    while j != i:
        game_list.append([i, j])
        i += 1
player_pieces = random.sample(game_list, 7)
for i in player_pieces:
    game_list.remove(i)
computer_pieces = random.sample(game_list, 7)
for i in computer_pieces:
    game_list.remove(i)
print("Stock size:", len(game_list))
print("Computer pieces:", len(computer_pieces))
snake = []


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


start_pieces()
for elem in snake:
    print(elem)


def status_check():
    if elem not in player_pieces and elem not in computer_pieces:
        print("Status: It's your turn to make a move. Enter your command.")
    elif elem in computer_pieces:
        print("Status: Computer is about to make a move. Press Enter to continue...")
        computer_pieces.remove(elem)


print("Your pieces:")


def draw_player_pieces():
    for elem1 in snake:
        if elem1 in player_pieces:
            player_pieces.remove(elem1)
    num = 0
    while num < len(player_pieces):
        num += 1
        print(str(num) + ":", player_pieces[num-1])


draw_player_pieces()
status_check()
