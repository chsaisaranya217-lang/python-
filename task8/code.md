# Manufacturing Cost and Profitability Analysis – Python Program

### 1. Problem Statement

Develop a Python program to calculate the total manufacturing cost by considering material costs, labour charges, wastage, and machine costs. Calculate the selling price and profit, and identify whether the production meets the specified profit target.

### 2. Algorithm

1. Start the program.
2. Enter material cost.
3. Enter labour charges.
4. Enter wastage percentage.
5. Enter machine cost.
6. Calculate wastage cost.
7. Calculate total manufacturing cost.
8. Enter selling price and profit target.
9. Calculate profit.
10. Check whether the profit meets the target.
11. Display the total cost, profit and result.
12. Stop.

### 3. Flowchart

Copy this flowchart:

```
          START
            |
            v
     Enter Material Cost
            |
            v
     Enter Labour Charges
            |
            v
      Enter Wastage %
            |
            v
       Enter Machine Cost
            |
            v
    Calculate Wastage Cost
            |
            v
 Calculate Total Manufacturing Cost
            |
            v
      Enter Selling Price
            |
            v
      Calculate Profit
            |
            v
   Enter Required Profit Target
            |
            v
       Is Profit >= Target?
          /       \
        YES        NO
         |          |
         v          v
   Target Met   Target Not Met
         \          /
          \        /
           v      v
       Display Result
            |
            v
           STOP
```

### 4. Python Source Code

```
material = float(input("Enter material cost: "))labour = float(input("Enter labour charges: "))wastage = float(input("Enter wastage percentage: "))machine = float(input("Enter machine cost: "))selling = float(input("Enter selling price: "))target = float(input("Enter profit target: "))waste_cost = material * wastage / 100total_cost = material + labour + waste_cost + machineprofit = selling - total_costprint("\n--- Manufacturing Report ---")print("Material Cost:", material)print("Labour Charges:", labour)print("Wastage Cost:", waste_cost)print("Machine Cost:", machine)print("Total Cost:", total_cost)print("Selling Price:", selling)print("Profit:", profit)if profit >= target:    print("Profit Target Achieved")else:    print("Profit Target Not Achieved")
```

### 5. Sample Input

```
Enter material cost: 5000
Enter labour charges: 2000
Enter wastage percentage: 10
Enter machine cost: 1000
Enter selling price: 10000
Enter profit target: 1000
```

### 6. Simple Output

```
--- Manufacturing Report ---
Material Cost: 5000
Labour Charges: 2000
Wastage Cost: 500.0
Machine Cost: 1000
Total Cost: 8500.0
Selling Price: 10000
Profit: 1500.0

Profit Target Achieved
```

### 7. Result

Thus, the Python program successfully calculates manufacturing costs, wastage, selling price and profit, and checks whether the required profit target is achieved.
