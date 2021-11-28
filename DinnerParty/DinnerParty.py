# Stage 1
number = int(input("Enter the number of friends joining (including you):\n> "))
d = {}
if number <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line")
    for i in range(number):
        name = input("> ")
        d.update({name: 0})
    print(d)
