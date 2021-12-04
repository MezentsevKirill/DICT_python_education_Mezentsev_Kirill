# Stage 1
action_list = ["rock", "paper", "scissors"]
user_str = input("Enter action\n> ")
if user_str == action_list[0]:
    print("Sorry, but the computer chose", action_list[1])
elif user_str == action_list[1]:
    print("Sorry, but the computer chose", action_list[2])
elif user_str == action_list[2]:
    print("Sorry, but the computer chose", action_list[0])
