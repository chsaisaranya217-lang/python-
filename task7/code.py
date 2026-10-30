n = int(input("Enter number of products: "))

total = 0

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    category = input("Enter category (food/clothing/electronics): ")

    amount = price * quantity

    if category == "food":
        tax = amount * 5 / 100
    elif category == "clothing":
        tax = amount * 5 / 100
    else:
        tax = amount * 18 / 100

    total = total + amount + tax

    print("Product:", name)
    print("Amount:", amount)
    print("Tax:", tax)

if total >= 5000:
    discount = total * 20 / 100
elif total >= 2000:
    discount = total * 10 / 100
else:
    discount = 0

if discount > 1000:
    discount = 1000

final_bill = total - discount

print("\n------ FINAL INVOICE ------")
print("Total Amount:", total)
print("Discount:", discount)
print("Final Bill:", final_bill)
