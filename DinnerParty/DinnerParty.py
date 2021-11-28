# Stage 1,2
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
    payment = amount / number
    for d_keys in d.keys():
        if amount % number == 0:
            d[d_keys] = payment
        elif amount % number > 0:
            d[d_keys] = "%.2f" % payment
    print(d)
