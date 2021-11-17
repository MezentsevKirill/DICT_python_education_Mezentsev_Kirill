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
# Stage 4
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--types", type=str)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=float)
args = parser.parse_args()
types = args.types
principal = args.principal
periods = args.periods
interest = args.interest
payment = args.payment
if types == "annuity":
    if types is not None and principal is not None and interest is not None and payment is not None:
        if principal > 0 and interest > 0 and payment > 0:
            i = interest / (12 * 100)
            import math
            n = math.log(payment / (payment - i * principal), i+1)
            if math.ceil(n) // 12 >= 1 and math.ceil(n) % 12 >= 1:
                print("It will take", math.ceil(n) // 12, "years and", math.ceil(n) % 12, "months to repay this loan!")
            elif math.ceil(n) // 12 >= 1 and math.ceil(n) % 12 == 0:
                print("It will take", math.ceil(n) // 12, "years to repay this loan!")
            elif math.ceil(n) // 12 == 0 and math.ceil(n) % 12 >= 1:
                print("It will take", math.ceil(n) % 12, "months to repay this loan!")
            print("Overpayment =", math.ceil(payment) * math.ceil(n) - math.ceil(principal))
        else:
            print("Incorrect parameters")
    elif types is not None and principal is not None and interest is not None and periods is not None:
        if principal > 0 and periods > 0 and interest > 0:
            import math
            i = interest / (12 * 100)
            payment = principal * ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
            print("Your monthly payment =", math.ceil(payment))
            print("Overpayment =", math.ceil(payment) * periods - math.ceil(principal))
        else:
            print("Incorrect parameters")
    elif types is not None and payment is not None and interest is not None and periods is not None:
        if periods > 0 and interest > 0 and payment > 0:
            import math
            i = interest / (12 * 100)
            principal = payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
            print("Your loan principal =", math.ceil(principal))
            print("Overpayment =", math.ceil(payment) * periods - math.ceil(principal))
        else:
            print("Incorrect parameters")
    elif periods and principal is None or periods and payment is None or periods and interest is None\
            or principal and interest is None or principal and payment is None:
        print("Incorrect parameters")
elif types == "diff":
    if types is not None and principal is not None and interest is not None and periods is not None:
        if principal > 0 and periods > 0 and interest > 0:
            import math
            i = interest / (12 * 100)
            months = 1
            m = 1
            overpayment = 0
            while m <= periods:
                d = principal / periods + i * (principal - ((principal * (m - 1)) / periods))
                print("Month", months, ": payment is", math.ceil(d))
                m += 1
                months += 1
                overpayment += d
            print("Overpayment =", math.ceil(overpayment) - principal)
        else:
            print("Incorrect parameters")
    elif types == "diff" and payment is not None:
        print("Incorrect parameters")
    elif periods and principal is None or periods and interest is None\
            or principal and interest is None:
        print("Incorrect parameters")
elif types is None:
    print("Incorrect parameters")
