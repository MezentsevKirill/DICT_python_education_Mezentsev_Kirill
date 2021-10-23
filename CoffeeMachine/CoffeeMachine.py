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
