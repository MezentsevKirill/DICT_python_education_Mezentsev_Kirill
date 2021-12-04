# Stage 1
import random
action_list = ["rock", "paper", "scissors", "!exit"]
result = ["lose", "draw", "win"]
user_str = None
while user_str != action_list[3]:
    user_str = input("Enter action\n> ")
    computer_str = random.choice(action_list)
    # Draw
    if user_str == action_list[0] and computer_str == action_list[0]:
        print("There is a draw", (action_list[0]))
    elif user_str == action_list[1] and computer_str == action_list[1]:
        print("There is a draw", (action_list[1]))
    elif user_str == action_list[2] and computer_str == action_list[2]:
        print("There is a draw", (action_list[2]))
    # Lose
    elif user_str == action_list[0] and computer_str == action_list[1]:
        print("Sorry, but the computer chose", (action_list[1]))
    elif user_str == action_list[1] and computer_str == action_list[2]:
        print("Sorry, but the computer chose", (action_list[2]))
    elif user_str == action_list[2] and computer_str == action_list[0]:
        print("Sorry, but the computer chose", (action_list[0]))
    # Win
    elif user_str == action_list[0] and computer_str == action_list[2]:
        print("Well done. The computer chose", (action_list[2]), "and failed")
    elif user_str == action_list[1] and computer_str == action_list[0]:
        print("Well done. The computer chose", (action_list[0]), "and failed")
    elif user_str == action_list[2] and computer_str == action_list[1]:
        print("Well done. The computer chose", (action_list[1]), "and failed")
    # Invalid input
    elif user_str not in action_list:
        print("Invalid input")
print("Bye!")
