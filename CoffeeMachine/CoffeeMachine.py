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
