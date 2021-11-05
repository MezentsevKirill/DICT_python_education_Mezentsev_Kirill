# Stage 1
print("X O X\n""O X O\n""X X O")
# Stage 2
game_list = []
user_str = str(input("Enter cells: "))
game_list.append(user_str)
game_list1 = list(game_list[0])


def draw_board():
    print("---------")
    print("|", game_list1[0], game_list1[1], game_list1[2], "|\n"
          "|", game_list1[3], game_list1[4], game_list1[5], "|\n"
          "|", game_list1[6], game_list1[7], game_list1[8], "|")
    print("---------")


draw_board()
