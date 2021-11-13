# Stage 1
print("Loan principal: 1000\nMonth 1: repaid 250\nMonth 2: repaid 250\nMonth 3: repaid 500\nThe loan has been repaid!")
# Stage 2
calculate_list = ["m", "p"]


def first_calculator():
    principal = int(input("Enter the loan principal:\n> "))
    calculate = input("What do you want to calculate?\ntype ""m"" – for number of monthly payments\n"
                      "type ""p"" – for the monthly payment:\n> ")
    if calculate == calculate_list[0]:
        monthly_payment = int(input("Enter the monthly payment:\n> "))
        months = principal // monthly_payment
        print("It will take", months, "months to repay the loan")
    elif calculate == calculate_list[1]:
        months = int(input("Enter the number of months:\n> "))
        import math
        monthly_payment = principal / months
        last_payment = principal - (months - 1) * math.ceil(monthly_payment)
        if math.ceil(monthly_payment) == last_payment:
            print("Your monthly payment =", math.ceil(monthly_payment))
        else:
            print("Your monthly payment =", math.ceil(monthly_payment), "and the last payment =",
                  math.ceil(last_payment))


first_calculator()
