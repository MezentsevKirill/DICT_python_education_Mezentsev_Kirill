# Stage 1
print("Starting to make a coffee\nGrinding coffee beans\nBoiling water")
print("Mixing boiled water with crushed coffee beans\nPouring coffee into the cup")
print("Pouring some milk into the cup\nCoffee is ready!")
# Stage 2
water = 200
milk = 50
coffee_beans = 15
amount_of_coffee = input("Write how many cups of coffee you will need: > ")
print("For", amount_of_coffee, "cups of coffee you will need:\n", int(amount_of_coffee) * water, "ml of water")
print(int(amount_of_coffee) * milk, "ml of milk\n", int(amount_of_coffee) * coffee_beans, "g of coffee beans")
# Stage 3
num_of_water = int(input("Write how many ml of water the coffee machine has: > "))
num_of_milk = int(input("Write how many ml of milk the coffee machine has: > "))
num_of_coffee_beans = int(input("Write how many grams of coffee beans the coffee machine has: > "))
amount_of_coffee = int(input("Write how many cups of coffee you will need: > "))
a = amount_of_coffee * water
b = amount_of_coffee * milk
c = amount_of_coffee * coffee_beans
if num_of_water >= a and num_of_milk >= b and num_of_coffee_beans >= c:
    print("Yes, I can make that amount of coffee")
n = (num_of_water + num_of_milk + num_of_coffee_beans) // (a + b + c)
if n > amount_of_coffee:
    print("Yes, I can make that amount of coffee (and even", n - amount_of_coffee, "more than that)")
if num_of_water < a and num_of_milk < b and num_of_coffee_beans < c:
    n = (num_of_water + num_of_milk + num_of_coffee_beans) // (water + milk + coffee_beans)
    print("No, I can make only", n, "cups of coffee")
# Stage 4
water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550
coffee_list = [1, 2, 3]
action_list = ["buy", "fill", "take"]
print("The coffee machine has:\n", water, "of water\n", milk, "of milk\n", coffee_beans, "of coffee beans")
print(disposable_cups, "of disposable cups\n", money, "of money")
action = input("Write action (buy, fill, take):\n > ")
if action == action_list[0]:
    coffee_class = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n > "))
    if coffee_class == coffee_list[0]:
        water1 = 250
        coffee_beans1 = 16
        disposable_cups1 = 1
        money1 = 4
        print("The coffee machine has:\n", water - water1, "of water")
        print(coffee_beans - coffee_beans1, "of coffee beans")
        print(disposable_cups - disposable_cups1, "of disposable cups\n", money + money1, "of money")
    if coffee_class == coffee_list[1]:
        water2 = 350
        milk2 = 75
        coffee_beans2 = 20
        disposable_cups2 = 1
        money2 = 7
        print("The coffee machine has:\n", water - water2, "of water\n", milk - milk2, "of milk")
        print(coffee_beans - coffee_beans2, "of coffee beans")
        print(disposable_cups - disposable_cups2, "of disposable cups\n", money + money2, "of money")
    if coffee_class == coffee_list[2]:
        water3 = 200
        milk3 = 100
        coffee_beans3 = 12
        disposable_cups3 = 1
        money3 = 6
        print("The coffee machine has:\n", water - water3, "of water\n", milk - milk3, "of milk")
        print(coffee_beans - coffee_beans3, "of coffee beans")
        print(disposable_cups - disposable_cups3, "of disposable cups\n", money + money3, "of money")
if action == action_list[1]:
    water_add = int(input("Write how many ml of water you want to add:\n > "))
    milk_add = int(input("Write how many ml of milk you want to add:\n > "))
    coffee_beans_add = int(input("Write how many grams of coffee beans you want to add:\n > "))
    disposable_cups_add = int(input("Write how many disposable coffee cups you want to add:\n > "))
    print("The coffee machine has:\n", water + water_add, "of water\n", milk + milk_add, "of milk")
    print(coffee_beans + coffee_beans_add, "of coffee beans")
    print(disposable_cups + disposable_cups_add, "of disposable cups\n", money, "of money")
if action == action_list[2]:
    print("I gave you", money)
    print("The coffee machine has:\n", water, "of water\n", milk, "of milk")
    print(coffee_beans, "of coffee beans\n", disposable_cups, "of disposable cups\n", money - money, "of money")
# Stage 5
coffee_list = ["1", "2", "3", "back"]
action_list = ["buy", "fill", "take", "remaining", "exit"]
water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550
while action != action_list[4]:
    action = input("Write action (buy, fill, take, remaining, exit):\n > ")
    if action == action_list[0]:
        coffee_class = str(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, cappuccino, back – to main menu:\n > "))
        if coffee_class == coffee_list[3]:
            action = 0
        if coffee_class == coffee_list[0]:
            water1 = 250
            coffee_beans1 = 16
            disposable_cups1 = 1
            money1 = 4
            if water > 250 and coffee_beans > 16 and disposable_cups > 1:
                print("I have enough resources, making you a coffee!")
                water -= water1
                coffee_beans -= coffee_beans1
                disposable_cups -= disposable_cups1
                money += money1
            else:
                if water < 250:
                    print("Sorry, not enough water!")
                if coffee_beans < 16:
                    print("Sorry, not enough coffee beans!")
                if disposable_cups < 1:
                    print("Sorry, not enough disposable cups!")
        if coffee_class == coffee_list[1]:
            water2 = 350
            milk2 = 75
            coffee_beans2 = 20
            disposable_cups2 = 1
            money2 = 7
            if water > 350 and milk > 75 and coffee_beans > 20 and disposable_cups > 1:
                print("I have enough resources, making you a coffee!")
                water -= water2
                milk -= milk2
                coffee_beans -= coffee_beans2
                disposable_cups -= disposable_cups2
                money += money2
            else:
                if water < 350:
                    print("Sorry, not enough water!")
                if milk < 75:
                    print("Sorry, not enough milk!")
                if coffee_beans < 20:
                    print("Sorry, not enough coffee beans!")
                if disposable_cups < 1:
                    print("Sorry, not enough disposable cups!")
        if coffee_class == coffee_list[2]:
            water3 = 200
            milk3 = 100
            coffee_beans3 = 12
            disposable_cups3 = 1
            money3 = 6
            if water > 200 and milk > 100 and coffee_beans > 12 and disposable_cups > 1:
                print("I have enough resources, making you a coffee!")
                water -= water3
                coffee_beans -= coffee_beans3
                disposable_cups -= disposable_cups3
                money += money3
            else:
                if water < 200:
                    print("Sorry, not enough water!")
                if milk < 100:
                    print("Sorry, not enough milk!")
                if coffee_beans < 12:
                    print("Sorry, not enough coffee beans!")
                if disposable_cups < 1:
                    print("Sorry, not enough disposable cups!")
    if action == action_list[1]:
        water_add = int(input("Write how many ml of water you want to add:\n > "))
        milk_add = int(input("Write how many ml of milk you want to add:\n > "))
        coffee_beans_add = int(input("Write how many grams of coffee beans you want to add:\n > "))
        disposable_cups_add = int(input("Write how many disposable coffee cups you want to add:\n > "))
        water += water_add
        milk += milk_add
        coffee_beans += coffee_beans_add
        disposable_cups += disposable_cups_add
    if action == action_list[2]:
        print("I gave you", money)
        money -= money
    if action == action_list[3]:
        print("The coffee machine has:\n", water, "of water\n", milk, "of milk")
        print(coffee_beans, "of coffee beans\n", disposable_cups, "of disposable cups\n", money, "of money")
