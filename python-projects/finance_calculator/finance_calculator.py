import math

# ---------------------------------------------
# Finance Calculator
# ---------------------------------------------
# This program calculates:
# 1. Simple or compound interest on an investment
# 2. Monthly repayment on a home loan (bond)
# ---------------------------------------------

print("Investment - To calculate the amount of interest you'll earn on your investment.")
print("Bond       - To calculate the amount you'll have to pay on a home loan.")

# Normalize user input
calculation_type = input(
    "Enter either 'investment' or 'bond' from the menu above to proceed: "
).strip().lower()

# ---------------------------------------------
# Investment Calculation
# ---------------------------------------------
if calculation_type == "investment":
    P = float(input("Enter the amount of money you are depositing: "))
    r = float(input("Enter the interest rate (as a percentage, no % needed): ")) / 100
    t = float(input("Enter the number of years you plan on investing: "))
    interest_type = input("Enter 'simple' or 'compound' interest: ").strip().lower()

    if interest_type == "simple":
        A = P * (1 + r * t)
    elif interest_type == "compound":
        A = P * math.pow((1 + r), t)
    else:
        print("Invalid interest type entered.")
        exit()

    print(f"\nThe total amount after {t} years is: {A:.2f}")

# ---------------------------------------------
# Bond Calculation
# ---------------------------------------------
elif calculation_type == "bond":
    P = float(input("Enter the present value of the house: "))
    r = float(input("Enter the interest rate (as a percentage): ")) / 100 / 12
    n = int(input("Enter the number of months to repay the bond: "))

    repayment = (r * P) / (1 - math.pow((1 + r), -n))

    print(f"\nYour monthly repayment amount is: {repayment:.2f}")

# ---------------------------------------------
# Invalid Selection
# ---------------------------------------------
else:
    print("Invalid calculation type entered.")
