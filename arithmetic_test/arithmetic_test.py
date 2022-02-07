from random import randint
import random
counter = 0
n = 0


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


while counter < 5:
    random_choice()
print("Your mark is", n, "/ 5")
