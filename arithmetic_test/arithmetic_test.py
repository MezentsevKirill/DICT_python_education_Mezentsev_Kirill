from random import randint
import random
counter = 0
n = 0


def writing_to_file():
    user_name = input("What is your name?\n> ")
    file = open("results.txt", "w", encoding="utf-8")
    file.write(f"{user_name}: {n}/5 in level {user_level}")
    file.close()


def random_choice():
    random_number1 = randint(2, 9)
    random_number2 = randint(2, 9)
    operations_list = [random_number1 + random_number2, random_number1 - random_number2,
                       random_number1 * random_number2]
    random_operations = random.choice(operations_list)
    if random_operations == operations_list[0]:
        print(random_number1, "+",  random_number2, "")
    elif random_operations == operations_list[1]:
        print(random_number1, "-",  random_number2, "")
    elif random_operations == operations_list[2]:
        print(random_number1, "*",  random_number2, "")

    def answers_check():
        try:
            user_choice = int(input("> "))
        except ValueError:
            print("Incorrect format")
        else:
            if user_choice == random_operations:
                print("Right!")
                global n
                n += 1
            else:
                print("Wrong!")
            global counter
            counter += 1

    answers_check()


user_level = input("Which level do you want? Enter a number:\n""1 - simple operations with numbers 2-9\n"
                   "2 - integral squares of 11-29\n> ")
if user_level == "1":
    while counter < 5:
        random_choice()
    print("Your mark is", n, "/ 5")
elif user_level == "2":
    while counter < 5:
        random_number3 = randint(11, 29)
        print(random_number3)
        try:
            user_choice2 = int(input("> "))
        except ValueError:
            print("Incorrect format")
        else:
            if user_choice2 == random_number3 ** 2:
                print("Right!")
                n += 1
            else:
                print("Wrong!")
            counter += 1
    print("Your mark is", n, "/ 5")
save_results = input("Would you like to save the result? Enter yes or no\n> ")
if save_results == "yes":
    writing_to_file()
    print("The results are saved in results.txt")
