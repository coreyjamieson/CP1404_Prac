"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    income_month = int(input("How many months? "))

    for month in range(1, income_month + 1):
        income = float(input("Enter income for month {0}: ".format(income_month)))
        incomes.append(income)

    report_print(income_month, incomes)


def report_print(income_month, incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, income_month + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()