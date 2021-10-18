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
# Stage 4
word = random.choice(my_list1)
# First if
if my_list1[0] == word:
    print("Guess the word: pyt--- > ")
    my_str2 = input()
    if my_str2 == my_list1[0]:
        print("You survived!")
    else:
        print("You lost")
# Second if
if my_list1[1] == word:
    print("Guess the word: jav- > ")
    my_str3 = input()
    if my_str3 == my_list1[1]:
        print("You survived!")
    else:
        print("You lost")
# Third if
if my_list1[2] == word:
    print("Guess the word: jav------- > ")
    my_str4 = input()
    if my_str4 == my_list1[2]:
        print("You survived")
    else:
        print("You lost")
# Fourth if
if my_list1[3] == word:
    print("Guess the word: --- > ")
    my_str5 = input()
    if my_str5 == my_list1[3]:
        print("You survived")
    else:
        print("You lost")
# Stage 5
new_word = random.choice(my_list1)
guessed_letters = []
word_completion = "_" * len(new_word)
guessed = False
tries = 8
while not guessed and tries > 0:
    print(word_completion)
    print("\n")
    guess = input("Input a letter: > ")
    guessed_letters.append(guess)
    word_as_list = list(word_completion)
    indices = [i for i, letter in enumerate(new_word) if letter == guess]
    for index in indices:
        word_as_list[index] = guess
        word_completion = "".join(word_as_list)
    if "_" not in word_completion:
        guessed = True
    if len(guess) == 1 and guess.isalpha():
        if guess in new_word:
            print("Good job,", guess, "is in the word!")
            print("\n")
            tries -= 1
        else:
            print("That letter doesn't appear in the word")
            tries -= 1
if word_completion == new_word:
    print("Thanks for playing!\nWe'll see how well you did in the next stage")
else:
    print("Sorry, you ran out of tries. The word was " + new_word + ". Maybe next time!")

# Stage 6
new_word = random.choice(my_list1)
guessed_letters = []
word_completion = "_" * len(new_word)
sliced_word = list(new_word)
guessed = False
tries = 8
while not guessed and tries > 0:
    print(word_completion)
    print("\n")
    guess = input("Input a letter: > ")
    guessed_letters.append(guess)
    word_as_list = list(word_completion)
    indices = [i for i, letter in enumerate(new_word) if letter == guess]
    for index in indices:
        word_as_list[index] = guess
        word_completion = "".join(word_as_list)
    if "_" not in word_completion:
        guessed = True
    if len(guess) == 1 and guess.isalpha():
        if guess in new_word:
            print("Good job,", guess, "is in the word!")
            print("\n")
        else:
            print("That letter doesn't appear in the word")
            tries -= 1
        for elem in guessed_letters:
            guessed_letters.count(guess)
            if guessed_letters.count(guess) > 2:
                print("No improvements")
                tries -= 1
if word_completion == new_word:
    print("You guessed the word!\nYou survived!")
else:
    print("Sorry, you ran out of tries. The word was " + new_word + ". Maybe next time!")

