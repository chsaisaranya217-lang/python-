# Multi-Plan Telecommunications Cost Optimization

## 1. Problem Statement

Write a Python program to compare different mobile recharge plans based on data usage, validity, and budget. Calculate extra charges for additional usage and identify the most economical plan that satisfies the user's requirements.

## 2. Algorithm

1. Start.
2. Enter monthly data usage.
3. Enter required validity days.
4. Enter maximum budget.
5. Enter mobile plan details.
6. Calculate extra data charges for each plan.
7. Calculate total plan cost.
8. Check validity and budget.
9. Select the cheapest eligible plan.
10. Display the best mobile plan.
11. Stop.

## 3. Flowchart

Copy this flowchart into your record.

```
          ┌──────────────┐
          │    START     │
          └──────┬───────┘
                 │
                 ▼
      ┌──────────────────────┐
      │ Enter Data Usage,    │
      │ Validity and Budget  │
      └──────────┬───────────┘
                 │
                 ▼
      ┌──────────────────────┐
      │ Enter Mobile Plan    │
      │ Details              │
      └──────────┬───────────┘
                 │
                 ▼
      ┌──────────────────────┐
      │ Calculate Extra      │
      │ Data Charges         │
      └──────────┬───────────┘
                 │
                 ▼
      ┌──────────────────────┐
      │ Calculate Total Cost │
      └──────────┬───────────┘
                 │
                 ▼
          ◇ Is Plan Within ◇
          ◇ Budget and     ◇
          ◇ Validity?      ◇
              /       \
            Yes        No
             │          │
             ▼          ▼
      ┌────────────┐  ┌─────────────┐
      │ Compare    │  │ Reject Plan │
      │ Plan Cost  │  └──────┬──────┘
      └─────┬──────┘         │
            └───────┬────────┘
                    │
                    ▼
       ┌────────────────────────┐
       │ Select Cheapest        │
       │ Eligible Plan          │
       └───────────┬────────────┘
                   │
                   ▼
       ┌────────────────────────┐
       │ Display Best Plan      │
       └───────────┬────────────┘
                   │
                   ▼
             ┌──────────┐
             │   STOP   │
             └──────────┘
```

## 4. Python Source Code

```
usage = int(input("Enter monthly data usage (GB): "))days = int(input("Enter required validity days: "))budget = int(input("Enter your budget: "))plans = [    ["Plan A", 199, 2, 28, 50],    ["Plan B", 299, 3, 56, 40],    ["Plan C", 399, 5, 84, 30]]best_cost = float('inf')best_plan = ""for plan in plans:    name, price, data, validity, extra = plan    extra_data = max(0, usage - data)    total = price + (extra_data * extra)    print("\n", name, "Total Cost:", total)    if validity >= days and total <= budget:        if total < best_cost:            best_cost = total            best_plan = nameprint("\n----- RESULT -----")if best_plan != "":    print("Best Plan:", best_plan)    print("Total Cost:", best_cost)else:    print("No eligible plan found")
```

## 5. Sample Input

```
Enter monthly data usage (GB): 4
Enter required validity days: 28
Enter your budget: 400
```

## 6. Sample Output

```
Plan A Total Cost: 299

Plan B Total Cost: 299

Plan C Total Cost: 399

----- RESULT -----
Best Plan: Plan A
Total Cost: 299
```

## 7. Result

Thus, the Python program successfully compares multiple mobile plans, calculates extra data charges, checks budget and validity, and identifies the most economical eligible plan.

Note: The mobile plan prices and data allowances are assumed values for this programming exercise.
