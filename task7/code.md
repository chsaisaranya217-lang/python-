# Retail Billing with Multiple Discount Rules – Python Program

### 1. Problem Statement

Develop a Python program to calculate the total bill for multiple products. The program should calculate product prices, quantities, category-based taxes, discounts based on purchase amount, and maximum discount limits. Finally, generate an itemized invoice.

### 2. Algorithm

1. Start the program.
2. Enter the number of products.
3. Enter product name, price, quantity and category.
4. Calculate subtotal for each product.
5. Apply tax based on product category.
6. Calculate the total amount.
7. Apply discount based on the purchase amount.
8. Apply the maximum discount limit.
9. Calculate the final bill.
10. Display the itemized invoice.
11. Stop.

### 3. Flowchart

Copy this flowchart directly:

```
          START
            |
            v
   Enter Number of Products
            |
            v
     Enter Product Details
            |
            v
    Calculate Subtotal
            |
            v
     Calculate Category Tax
            |
            v
     Calculate Total Amount
            |
            v
    Check Discount Threshold
            |
            v
      Apply Discount
            |
            v
   Check Maximum Discount Limit
            |
            v
     Calculate Final Bill
            |
            v
     Display Itemized Invoice
            |
            v
           STOP
```

### 4. Python Source Code

```
n = int(input("Enter number of products: "))total = 0for i in range(n):    print("\nProduct", i + 1)    name = input("Enter product name: ")    price = float(input("Enter price: "))    quantity = int(input("Enter quantity: "))    category = input("Enter category (food/clothing/electronics): ")    amount = price * quantity    if category == "food":        tax = amount * 5 / 100    elif category == "clothing":        tax = amount * 5 / 100    else:        tax = amount * 18 / 100    total = total + amount + tax    print("Product:", name)    print("Amount:", amount)    print("Tax:", tax)if total >= 5000:    discount = total * 20 / 100elif total >= 2000:    discount = total * 10 / 100else:    discount = 0if discount > 1000:    discount = 1000final_bill = total - discountprint("\n------ FINAL INVOICE ------")print("Total Amount:", total)print("Discount:", discount)print("Final Bill:", final_bill)
```

### 5. Sample Input

```
Enter number of products: 2

Product 1
Enter product name: Shirt
Enter price: 1000
Enter quantity: 2
Enter category: clothing

Product 2
Enter product name: Mobile
Enter price: 5000
Enter quantity: 1
Enter category: electronics
```

### 6. Simple Output

```
Product: Shirt
Amount: 2000
Tax: 100

Product: Mobile
Amount: 5000
Tax: 900

------ FINAL INVOICE ------
Total Amount: 8000
Discount: 1000
Final Bill: 7000
```

### 7. Result

Thus, the Python program successfully calculates the retail bill using product quantities, category-based taxes, discount rules and maximum discount limits.
