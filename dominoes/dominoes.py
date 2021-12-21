import random
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
print("Stock pieces:", game_list)
print("Player pieces:", player_pieces)
print("Computer pieces:", computer_pieces)
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
    print("Domino snake:", elem)


def status_check():
    if elem in player_pieces:
        print("Status: player")
    elif elem in computer_pieces:
        print("Status: computer")


status_check()
