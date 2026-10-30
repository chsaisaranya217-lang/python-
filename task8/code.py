material = float(input("Enter material cost: "))
labour = float(input("Enter labour charges: "))
wastage = float(input("Enter wastage percentage: "))
machine = float(input("Enter machine cost: "))

selling = float(input("Enter selling price: "))
target = float(input("Enter profit target: "))

waste_cost = material * wastage / 100

total_cost = material + labour + waste_cost + machine

profit = selling - total_cost

print("\n--- Manufacturing Report ---")
print("Material Cost:", material)
print("Labour Charges:", labour)
print("Wastage Cost:", waste_cost)
print("Machine Cost:", machine)
print("Total Cost:", total_cost)
print("Selling Price:", selling)
print("Profit:", profit)

if profit >= target:
    print("Profit Target Achieved")
else:
    print("Profit Target Not Achieved")
