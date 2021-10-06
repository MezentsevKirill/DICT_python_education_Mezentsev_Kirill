# Stage 1
print("HANGMAN")
print("The game will be available soon")
# Stage 2
my_list = ["python"]
my_str = input("Guess the word: > ")
if my_str in my_list:
    print("You survived!")
else:
    print("You lost!")
# Stage 3
import random
my_list1 = ["python", "java", "javascript", "php"]
my_str1 = input("Guess the word: > ")
if my_str1 == random.choice(my_list1):
    print("You survived!")
else:
    print("You lost")
