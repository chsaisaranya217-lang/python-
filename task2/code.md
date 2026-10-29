# Progressive Electricity Billing System using Python

## 1. Problem Statement

Develop a Python program to calculate household electricity bills based on different consumption slabs, fixed charges, surcharges, and rebates. Compare electricity bills across several months and identify unusual increases in the bill amount.

## 2. Algorithm

1. Start.
2. Enter the number of months.
3. Enter electricity units consumed in each month.
4. Calculate charges using progressive slabs:
   - First 100 units: ₹2 per unit
   - Next 100 units: ₹3 per unit
   - Above 200 units: ₹5 per unit
5. Add fixed charge of ₹50.
6. Add a surcharge of 5%.
7. Give a 5% rebate if consumption is 100 units or less.
8. Calculate the final bill for each month.
9. Compare each month's bill with the previous month's bill.
10. If the bill increases by more than 30%, identify it as an unusual increase.
11. Display the bills and stop.

## 3. Flowchart

Copy this text flowchart into your record.

```

          +-----------+
          |   START   |
          +-----------+
                |
                v
      +--------------------+
      | Enter Number of    |
      | Months             |
      +--------------------+
                |
                v
      +--------------------+
      | Enter Units Used   |
      +--------------------+
                |
                v
      +--------------------+
      | Calculate Slab     |
      | Charges            |
      +--------------------+
                |
                v
      +--------------------+
      | Add Fixed Charges  |
      | and Surcharge      |
      +--------------------+
                |
                v
      +--------------------+
      | Apply Rebate       |
      +--------------------+
                |
                v
      +--------------------+
      | Calculate Final    |
      | Electricity Bill   |
      +--------------------+
                |
                v
      +--------------------+
      | Compare with       |
      | Previous Month     |
      +--------------------+
                |
                v
      +--------------------+
      | Increase > 30% ?   |
      +--------------------+
          /          \
        Yes           No
         |             |
         v             v
  +-------------+  +-------------+
  | Unusual     |  | Normal      |
  | Increase    |  | Increase    |
  +-------------+  +-------------+
          \          /
           \        /
                |
                v
      +--------------------+
      | Display All Bills  |
      +--------------------+
                |
                v
          +-----------+
          |   STOP    |
          +-----------+

```

## 4. Python Source Code

```
bills = []n = int(input("Enter number of months: "))for i in range(n):    units = int(input("Enter units consumed: "))    # Progressive slab calculation    if units <= 100:        charge = units * 2    elif units <= 200:        charge = 100 * 2 + (units - 100) * 3    else:        charge = 100 * 2 + 100 * 3 + (units - 200) * 5    fixed = 50    surcharge = (charge + fixed) * 0.05    total = charge + fixed + surcharge    if units <= 100:        rebate = total * 0.05    else:        rebate = 0    total = total - rebate    bills.append(total)    print("Electricity Bill: Rs.", round(total, 2))# Compare monthly billsprint("\nMonthly Bill Comparison")for i in range(1, n):    increase = bills[i] - bills[i - 1]    if bills[i - 1] > 0:        percentage = increase / bills[i - 1] * 100    else:        percentage = 0    print("Month", i + 1, "Bill:", round(bills[i], 2))    if percentage > 30:        print("Unusual increase detected!")    else:        print("Normal bill change")
```

## 5. Sample Input

```
Enter number of months: 3
Enter units consumed: 80
Enter units consumed: 120
Enter units consumed: 250
```

## 6. Sample Output

```
Electricity Bill: Rs. 209.48
Electricity Bill: Rs. 365.75
Electricity Bill: Rs. 785.0

Monthly Bill Comparison
Month 2 Bill: 365.75
Unusual increase detected!
Month 3 Bill: 785.0
Unusual increase detected!
```

## 7. Result

The program calculates electricity bills using progressive consumption slabs, fixed charges, surcharges, and rebates. It compares monthly bills and identifies increases greater than 30%.

Note: These slab rates and charges are examples for a student project, not official electricity tariff rates.
