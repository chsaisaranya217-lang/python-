budget = float(input("Enter travel budget in INR: "))

n = int(input("Enter number of expenses: "))

total = 0
largest = 0
largest_category = ""

for i in range(n):

    print("\nExpense", i + 1)

    category = input("Enter category: ")
    amount = float(input("Enter expense amount: "))
    rate = float(input("Enter exchange rate: "))

    converted = amount * rate

    fee = converted * 2 / 100

    final = converted + fee

    total = total + final

    if final > largest:
        largest = final
        largest_category = category

    print("Converted Amount:", converted)
    print("Conversion Fee:", fee)
    print("Total Expense:", final)

print("\n--- TRAVEL BUDGET REPORT ---")

print("Total Expenses:", total)
print("Travel Budget:", budget)
print("Largest Expense:", largest_category)

if total <= budget:
    print("Status: Within Budget")
else:
    print("Status: Over Budget")

print("Remaining Budget:", budget - total)
