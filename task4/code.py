name = input("Enter employee name: ")

basic = float(input("Enter basic pay: "))
allowance = float(input("Enter allowance: "))
overtime = float(input("Enter overtime: "))
incentive = float(input("Enter incentive: "))

gross = basic + allowance + overtime + incentive

if gross <= 10000:
    tax = 0
elif gross <= 20000:
    tax = (gross - 10000) * 0.05
else:
    tax = 500 + (gross - 20000) * 0.10

net = gross - tax

print("\n----- SALARY STATEMENT -----")
print("Employee Name:", name)
print("Basic Pay:", basic)
print("Allowance:", allowance)
print("Overtime:", overtime)
print("Incentive:", incentive)
print("Gross Salary:", gross)
print("Tax Deduction:", tax)
print("Net Salary:", net)
