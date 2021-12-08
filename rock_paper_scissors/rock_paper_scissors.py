# Stage 1, 2, 3, 4
import random
action_list = ["rock", "paper", "scissors", "!exit", "!rating"]
result = ["lose", "draw", "win"]
user_name = input("Enter yor name:> ")
print("Hello", user_name)
file = open("rating.txt", "r", encoding="utf-8")
if file.read(4) == user_name:
    rating = 350
else:
    file.seek(8)
    if user_name == file.read(4):
        rating = 200
    else:
        file.seek(16)
        if user_name == file.read(6):
            rating = 400
        else:
            rating = 0
file.close()
user_str = None
while user_str != action_list[3]:
    user_str = input("Enter action\n> ")
    computer_str = random.choice(action_list)
    # Draw
    if user_str == action_list[0] and computer_str == action_list[0]:
        print("There is a draw", (action_list[0]))
        rating += 50
    elif user_str == action_list[1] and computer_str == action_list[1]:
        print("There is a draw", (action_list[1]))
        rating += 50
    elif user_str == action_list[2] and computer_str == action_list[2]:
        print("There is a draw", (action_list[2]))
        rating += 50
    # Lose
    if user_str == action_list[0] and computer_str == action_list[1]:
        print("Sorry, but the computer chose", (action_list[1]))
    elif user_str == action_list[1] and computer_str == action_list[2]:
        print("Sorry, but the computer chose", (action_list[2]))
    elif user_str == action_list[2] and computer_str == action_list[0]:
        print("Sorry, but the computer chose", (action_list[0]))
    # Win
    if user_str == action_list[0] and computer_str == action_list[2]:
        print("Well done. The computer chose", (action_list[2]), "and failed")
        rating += 100
    elif user_str == action_list[1] and computer_str == action_list[0]:
        print("Well done. The computer chose", (action_list[0]), "and failed")
        rating += 100
    elif user_str == action_list[2] and computer_str == action_list[1]:
        print("Well done. The computer chose", (action_list[1]), "and failed")
        rating += 100
    # Invalid input
    elif user_str not in action_list:
        print("Invalid input")
    elif user_str == action_list[4]:
        print("Your rating:", rating)
print("Bye!")
