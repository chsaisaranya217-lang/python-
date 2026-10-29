
bills = []
n = int(input("Enter number of months: "))

for i in range(n):
    units = int(input("Enter units consumed: "))

    # Progressive slab calculation
    if units <= 100:
        charge = units * 2
    elif units <= 200:
        charge = 100 * 2 + (units - 100) * 3
    else:
        charge = 100 * 2 + 100 * 3 + (units - 200) * 5

    fixed = 50
    surcharge = (charge + fixed) * 0.05
    total = charge + fixed + surcharge

    if units <= 100:
        rebate = total * 0.05
    else:
        rebate = 0

    total = total - rebate
    bills.append(total)

    print("Electricity Bill: Rs.", round(total, 2))

print("\nMonthly Bill Comparison")

for i in range(1, n):
    increase = bills[i] - bills[i - 1]

    if bills[i - 1] > 0:
        percentage = increase / bills[i - 1] * 100
    else:
        percentage = 0

    print("Month", i + 1, "Bill:", round(bills[i], 2))

    if percentage > 30:
        print("Unusual increase detected!")
    else:
        print("Normal bill change")

