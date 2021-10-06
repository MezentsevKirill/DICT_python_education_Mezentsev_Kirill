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
