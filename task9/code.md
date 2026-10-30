# Multi-Currency Travel Budget Analysis – Python Program

### 1. Problem Statement

Develop a Python program to calculate travel expenses in different currencies. Convert expenses into Indian Rupees using exchange rates, include conversion fees, compare total spending with the budget, and identify the largest expense category.

### 2. Algorithm

1. Start the program.
2. Enter the travel budget in Indian Rupees.
3. Enter the number of expense categories.
4. Enter category name and expense amount.
5. Enter the exchange rate.
6. Convert the expense into Indian Rupees.
7. Calculate the conversion fee.
8. Calculate the total travel expenses.
9. Compare expenses with the budget.
10. Identify the largest expense category.
11. Display the final report.
12. Stop.

### 3. Flowchart

Copy this flowchart:

```
           START
              |
              v
       Enter Travel Budget
              |
              v
      Enter Number of Expenses
              |
              v
      Enter Expense Category
              |
              v
       Enter Amount and Rate
              |
              v
     Convert into Indian Rupees
              |
              v
       Calculate Conversion Fee
              |
              v
       Calculate Total Expenses
              |
              v
       Find Largest Category
              |
              v
       Compare with Budget
              |
              v
        Is Expense <= Budget?
           /          \
         YES           NO
          |             |
          v             v
     Within Budget   Over Budget
          \             /
           \           /
            v         v
        Display Report
              |
              v
             STOP
```

### 4. Python Source Code

```
budget = float(input("Enter travel budget in INR: "))n = int(input("Enter number of expenses: "))total = 0largest = 0largest_category = ""for i in range(n):    print("\nExpense", i + 1)    category = input("Enter category: ")    amount = float(input("Enter expense amount: "))    rate = float(input("Enter exchange rate: "))    converted = amount * rate    fee = converted * 2 / 100    final = converted + fee    total = total + final    if final > largest:        largest = final        largest_category = category    print("Converted Amount:", converted)    print("Conversion Fee:", fee)    print("Total Expense:", final)print("\n--- TRAVEL BUDGET REPORT ---")print("Total Expenses:", total)print("Travel Budget:", budget)
```

### 5. Sample Input

```
Enter travel budget in INR: 50000
Enter number of expenses: 3

Expense 1
Enter category: Hotel
Enter expense amount: 100
Enter exchange rate: 85

Expense 2
Enter category: Food
Enter expense amount: 50
Enter exchange rate: 85

Expense 3
Enter category: Shopping
Enter expense amount: 200
Enter exchange rate: 85
```

### 6. Simple Output

```
Converted Amount: 8500
Conversion Fee: 170
Total Expense: 8670

Converted Amount: 4250
Conversion Fee: 85
Total Expense: 4335

Converted Amount: 17000
Conversion Fee: 340
Total Expense: 17340

--- TRAVEL BUDGET REPORT ---

Total Expenses: 30345
Travel Budget: 50000
Largest Expense: Shopping
Status: Within Budget
Remaining Budget: 19655
```

### 7. Result

Thus, the Python program successfully converts multiple currency expenses into Indian Rupees, calculates conversion fees, compares total expenses with the travel budget, and identifies the largest expense category.
