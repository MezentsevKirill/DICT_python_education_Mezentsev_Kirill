# Stage 1
print("X O X\n""O X O\n""X X O")
# Stage 2
game_list = []
user_str = str(input("Enter cells: "))
game_list.append(user_str)
game_list = list(game_list[0])


def draw_board():
    print("---------")
    print("|", game_list[0], game_list[1], game_list[2], "|\n"
          "|", game_list[3], game_list[4], game_list[5], "|\n"
          "|", game_list[6], game_list[7], game_list[8], "|")
    print("---------")


draw_board()
# Stage 3
game_list.clear()
user_str = str(input("Enter cells: "))
game_list.append(user_str)
x = ["X", "X", "X"]
o = ["O", "O", "O"]
none = ["_"]
win_coord = [game_list[0:3], game_list[3:6], game_list[6:], game_list[0:None:3], game_list[1:None:3],
             game_list[2:None:3], game_list[0:None:4], game_list[-7:-1:2]]
game_list = list(game_list[0])
draw_board()
if game_list[0:3] == x or game_list[3:6] == x or game_list[6:] == x or game_list[0:None:3] == x\
            or game_list[1:None:3] == x or game_list[2:None:3] == x\
            or game_list[0:None:4] == x or game_list[-7:-1:2] == x:
    print("X wins")
elif game_list[0:3] == o or game_list[3:6] == o or game_list[6:] == o or game_list[0:None:3] == o\
            or game_list[1:None:3] == o or game_list[2:None:3] == o\
            or game_list[0:None:4] == o or game_list[-7:-1:2] == o:
    print("0 wins")
elif game_list[0:3] == x and game_list[3:6] == o or game_list[0:3] == x or o and game_list[6:] == o\
        or game_list[0:3] == o and game_list[3:6] == x or game_list[0:3] == o or o and game_list[6:] == x\
        or game_list[3:6] == x and game_list[0:3] == o or game_list[3:6] == x and game_list[6:] == o\
        or game_list[3:6] == o and game_list[0:3] == x or game_list[3:6] == o and game_list[6:] == x\
        or game_list[0:None:3] == x and game_list[1:None:3] == o\
        or game_list[0:None:3] == x and game_list[2:None:3] == o\
        or game_list[0:None:3] == o and game_list[1:None:3] == x\
        or game_list[0:None:3] == o and game_list[2:None:3] == x\
        or game_list[1:None:3] == x and game_list[0:None:3] == o\
        or game_list[1:None:3] == x and game_list[2:None:3] == o\
        or game_list[1:None:3] == o and game_list[0:None:3] == x\
        or game_list[1:None:3] == o and game_list[2:None:3] == x\
        or game_list.count("O") > game_list.count("X") + 1\
        or game_list.count("X") > game_list.count("O") + 1:
    print("impossible")
elif "_" not in game_list and game_list[0:3] != x and o or "_" not in game_list and game_list[3:6] != x and o\
            or "_" not in game_list and game_list[6:] != x and o\
            or "_" not in game_list and game_list[0:None:3] != x and o\
            or "_" not in game_list and game_list[1:None:3] != x and o\
            or "_" not in game_list and game_list[2:None:3] != x and o\
            or "_" not in game_list and game_list[0:None:4] != x and o\
            or "_" not in game_list and game_list[-7:-1:2] != x and o:
    print("Draw")
elif "_" in game_list and game_list[0:3] != x and o or "_" not in game_list and game_list[3:6] != x and o\
            or "_" in game_list and game_list[6:] != x and o\
            or "_" in game_list and game_list[0:None:3] != x and o\
            or "_" in game_list and game_list[1:None:3] != x and o\
            or "_" in game_list and game_list[2:None:3] != x and o\
            or "_" in game_list and game_list[0:None:4] != x and o\
            or "_" in game_list and game_list[-7:-1:2] != x and o:
    print("Game not finished")
