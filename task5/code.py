usage = int(input("Enter monthly data usage (GB): "))
days = int(input("Enter required validity days: "))
budget = int(input("Enter your budget: "))

plans = [
    ["Plan A", 199, 2, 28, 50],
    ["Plan B", 299, 3, 56, 40],
    ["Plan C", 399, 5, 84, 30]
]

best_cost = float('inf')
best_plan = ""

for plan in plans:
    name, price, data, validity, extra = plan

    extra_data = max(0, usage - data)
    total = price + (extra_data * extra)

    print("\n", name, "Total Cost:", total)

    if validity >= days and total <= budget:
        if total < best_cost:
            best_cost = total
            best_plan = name

print("\n----- RESULT -----")

if best_plan != "":
    print("Best Plan:", best_plan)
    print("Total Cost:", best_cost)
else:
    print("No eligible plan found")
