# Employee Payroll and Deduction Analysis

## 1. Problem Statement

Write a Python program to calculate an employee's gross salary using basic pay, allowances, overtime, and incentives. Apply progressive tax deductions and generate a formatted salary statement showing gross salary, total deductions, and net salary.

## 2. Algorithm

1. Start.
2. Enter employee name.
3. Enter basic pay, allowances, overtime, and incentives.
4. Calculate gross salary.
5. Calculate progressive tax:
   - First ₹10,000 – No tax.
   - Next ₹10,000 – 5% tax.
   - Above ₹20,000 – 10% tax.
6. Calculate net salary.
7. Display the salary statement.
8. Stop.

## 3. Flowchart
          ┌─────────────┐
          │    START    │
          └──────┬──────┘
                 │
                 ▼
       ┌─────────────────────┐
       │ Enter Employee Name │
       └─────────┬───────────┘
                 │
                 ▼
       ┌─────────────────────┐
       │ Enter Basic Pay,    │
       │ Allowance, Overtime │
       │ and Incentive       │
       └─────────┬───────────┘
                 │
                 ▼
       ┌─────────────────────┐
       │ Calculate Gross     │
       │ Salary              │
       └─────────┬───────────┘
                 │
                 ▼
       ┌─────────────────────┐
       │ Calculate Tax       │
       │ Deduction           │
       └─────────┬───────────┘
                 │
                 ▼
       ┌─────────────────────┐
       │ Calculate Net       │
       │ Salary              │
       └─────────┬───────────┘
                 │
                 ▼
       ┌─────────────────────┐
       │ Display Salary      │
       │ Statement           │
       └─────────┬───────────┘
                 │
                 ▼
          ┌─────────────┐
          │    STOP     │
          └─────────────┘

## 4. Python Source Code

```
name = input("Enter employee name: ")basic = float(input("Enter basic pay: "))allowance = float(input("Enter allowance: "))overtime = float(input("Enter overtime: "))incentive = float(input("Enter incentive: "))gross = basic + allowance + overtime + incentiveif gross <= 10000:    tax = 0elif gross <= 20000:    tax = (gross - 10000) * 0.05else:    tax = 500 + (gross - 20000) * 0.10net = gross - taxprint("\n----- SALARY STATEMENT -----")print("Employee Name:", name)print("Basic Pay:", basic)print("Allowance:", allowance)print("Overtime:", overtime)print("Incentive:", incentive)print("Gross Salary:", gross)print("Tax Deduction:", tax)print("Net Salary:", net)
```

## 5. Sample Input

```
Enter employee name: Ravi
Enter basic pay: 20000
Enter allowance: 5000
Enter overtime: 2000
Enter incentive: 1000
```

## 6. Simple Output

```
----- SALARY STATEMENT -----

Employee Name: Ravi
Basic Pay: 20000
Allowance: 5000
Overtime: 2000
Incentive: 1000
Gross Salary: 28000
Tax Deduction: 1300
Net Salary: 26700
```

## 7. Result

Thus, the Python program successfully calculates the employee's gross salary, progressive tax deduction, and net salary and displays a formatted salary statement.

Note: The tax slabs are assumed for this programming exercise and are not actual income-tax rules.
