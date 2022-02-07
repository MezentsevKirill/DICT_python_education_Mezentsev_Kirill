from random import randint
import random


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
        user_choice = int(input("> "))
        if user_choice == random_operations:
            print("Right!")
        else:
            print("Wrong!")

    answers_check()


random_choice()
