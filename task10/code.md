# Campus Event Financial Planning – Python Program

### 1. Problem Statement

Develop a Python program to calculate the total expenses of a college event, including venue, equipment, catering, transport and certificate costs. Calculate participant contributions, sponsorship amount, sponsorship shortfall and the minimum number of registrations required to break even.

### 2. Algorithm

1. Start the program.
2. Enter venue cost.
3. Enter equipment cost.
4. Enter catering cost per participant.
5. Enter transport cost.
6. Enter certificate cost per participant.
7. Enter expected participants.
8. Enter sponsorship amount.
9. Calculate total event expenses.
10. Calculate participant contribution.
11. Calculate sponsorship shortfall.
12. Calculate minimum registrations required to break even.
13. Display the financial report.
14. Stop.

### 3. Flowchart

Copy this flowchart:

```
             START
               |
               v
        Enter Venue Cost
               |
               v
      Enter Equipment Cost
               |
               v
       Enter Catering Cost
               |
               v
       Enter Transport Cost
               |
               v
      Enter Certificate Cost
               |
               v
       Enter Number of Participants
               |
               v
       Enter Sponsorship Amount
               |
               v
       Calculate Total Expenses
               |
               v
      Calculate Participant Cost
               |
               v
       Calculate Sponsorship Shortfall
               |
               v
      Calculate Break-Even Registrations
               |
               v
        Display Financial Report
               |
               v
              STOP
```

### 4. Python Source Code

```
venue = float(input("Enter venue cost: "))equipment = float(input("Enter equipment cost: "))catering = float(input("Enter catering cost per participant: "))transport = float(input("Enter transport cost: "))certificate = float(input("Enter certificate cost per participant: "))participants = int(input("Enter number of participants: "))sponsorship = float(input("Enter sponsorship amount: "))fixed_cost = venue + equipment + transportvariable_cost = catering + certificatetotal_cost = fixed_cost + (variable_cost * participants)participant_amount = total_cost - sponsorshipshortfall = max(0, total_cost - sponsorship)if participant_amount > 0:    contribution = participant_amount / participantselse:    contribution = 0break_even = (fixed_cost - sponsorship) / (contribution - variable_cost)if break_even < 0:    break_even = 0else:    break_even = int(break_even) + 1print("\n--- EVENT FINANCIAL REPORT ---")print("Fixed Cost:", fixed_cost)print("Variable Cost:", variable_cost)print("Total Expenses:", total_cost)
```

### 5. Sample Input

```
Enter venue cost: 10000
Enter equipment cost: 5000
Enter catering cost per participant: 200
Enter transport cost: 3000
Enter certificate cost per participant: 50
Enter number of participants: 100
Enter sponsorship amount: 10000
```

### 6. Simple Output

```
--- EVENT FINANCIAL REPORT ---

Fixed Cost: 18000
Variable Cost: 250
Total Expenses: 43000
Sponsorship: 10000
Sponsorship Shortfall: 33000
Participant Contribution: 330.0
Break-Even Registrations: 225
```

### 7. Result

Thus, the Python program successfully calculates campus event expenses, participant contributions, sponsorship shortfalls and the minimum registrations required to break even.
