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
# Stage 3
new_calculate_list = ["n", "a", "p"]


def second_calculator():
    calculate = input("What do you want to calculate?\ntype ""n"" – for number of monthly payments\n"
                      "type ""a"" – for annuity monthly payment amount:\n"
                      "type ""p"" - for loan principal:\n> ")
    if calculate == new_calculate_list[0]:
        p = int(input("Enter the loan principal:\n> "))
        a = int(input("Enter the monthly payment:\n> "))
        loan_interest = int(input("Enter the loan interest:\n > "))
        import math
        i = loan_interest / (12 * 100)
        n = math.log(a / (a - i * p), i+1)
        if math.ceil(n) // 12 >= 1 and math.ceil(n) % 12 >= 1:
            print("It will take", math.ceil(n) // 12, "years and", math.ceil(n) % 12, "months to repay this loan!")
        elif math.ceil(n) // 12 >= 1 and math.ceil(n) % 12 == 0:
            print("It will take", math.ceil(n) // 12, "years to repay this loan!")
        elif math.ceil(n) // 12 == 0 and math.ceil(n) % 12 >= 1:
            print("It will take", math.ceil(n) % 12, "months to repay this loan!")
    if calculate == new_calculate_list[1]:
        import math
        p = int(input("Enter the loan principal:\n> "))
        n = int(input("Enter the numbers of periods:\n> "))
        loan_interest = int(input("Enter the loan interest:\n> "))
        i = loan_interest / (12 * 100)
        a = p * ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
        print("Your monthly payment =", math.ceil(a))
    if calculate == new_calculate_list[2]:
        import math
        a = float(input("Enter the annuity payment:\n> "))
        n = int(input("Enter the numbers of periods:\n> "))
        loan_interest = float(input("Enter the loan interest:\n> "))
        i = loan_interest / (12 * 100)
        p = a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
        print("Your loan principal =", math.ceil(p))


second_calculator()
