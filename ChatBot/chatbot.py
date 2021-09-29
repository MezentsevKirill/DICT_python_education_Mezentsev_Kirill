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
# Stage 4
print("Now I will prove to you that I can count to any number you want")
num = int(input("< "))
x = int()
while x <= num:
    print("" + str(x) + "!")
    x += 1
print("Completed, have a nice day!")
# Stage 5
print("Let's test your programming knowledge")
print("Which companies provide the most popular cloud services?")
print("1. Google")
print("2. Adobe")
print("3. Steam")
print("4. Mozilla")
chek = False
while (chek == False):
    a = int(input("< "))
    if a == 1:
        chek = True
        print("Completed, have a nice day!")
    else:
        print("Please, try again")

print("Congratulations, have a nice day!")
