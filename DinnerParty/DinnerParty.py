# Stage 1,2
import random
number = int(input("Enter the number of friends joining (including you):\n> "))
d = {}
if number <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line")
    for i in range(number):
        name = input("> ")
        d.update({name: 0})
    amount = int(input("Enter the total amount:\n> "))
    lucky = input("Do you want to use the "'Who is lucky?'" feature? Write Yes/No:\n> ")
    if lucky == "No":
        payment = amount / number
        for d_keys in d.keys():
            if amount % number == 0:
                d[d_keys] = payment
            elif amount % number > 0:
                d[d_keys] = "%.2f" % payment
        print("No one is going to be lucky")
    elif lucky == "Yes":
        payment = amount / (number - 1)
        lucky_one = random.choice(list(d.keys()))
        for d_keys in d.keys():
            if amount % number == 0:
                d[d_keys] = payment
            elif amount % (number-1) > 0:
                d[d_keys] = "%.2f" % payment
            d[lucky_one] = 0
        print(lucky_one, "is the lucky one!")
    print(d)
