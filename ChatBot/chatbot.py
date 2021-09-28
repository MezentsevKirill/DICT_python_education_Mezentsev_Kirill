# Stage 1
print("Hello! My name is DICT_Bot")
print("I was created in 2021")
# Stage 2
print("Please, remind me your name")
name = input("< ")
print("What a great name you have, " + name + "!")
# Stage 3
print("Let me guess your age")
print("Enter remainders of dividing your age by 3, 5 and 7")
my_str = input("< ")
my_str1 = input("< ")
my_str2 = input("< ")
age = (int(my_str) * 70 + int(my_str1) * 21 + int(my_str2) * 15) % 105
print("Your age is " + str(age) + "!"",that's a good time to start programming!")
