

for i in range(1, 21, 2):
    print(i, end=' ')
print()

for j in range(0, 101, 10):
    print(j , end=' ')
print()

for k in range(20, 0, -1):
    print(k, end=' ')
print()


sales = float(input("Enter sales $: "))
while sales <= 0:
    print("Invalid Input")
    sales = float(input("Enter sales $: "))
    if sales < 1000:
        print("10% Bonus")
        bonus = sales * 0.1
        print("$: ", bonus, "is your bonus. Total $: ", bonus + sales)
    elif sales >= 1000:
        print("15% Bonus")
        bonus = sales * 0.15
        print("$: ", bonus, "is your bonus. Total $: ", bonus + sales)
