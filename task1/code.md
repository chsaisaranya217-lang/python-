# University Scholarship Allocation System using Python

## 1. Problem Statement

Design a Python program to select eligible students for university scholarships based on aggregate marks, subject-wise minimum marks, attendance percentage, and family income. The program ranks eligible students and resolves ties using predefined rules.

## 2. Algorithm

1. Start.
2. Enter the number of students.
3. Enter each student's name, aggregate marks, subject marks, attendance, and family income.
4. Check the eligibility conditions:
   - Aggregate marks must be at least 75%.
   - Every subject mark must be at least 40.
   - Attendance must be at least 75%.
   - Annual family income must be ₹2,00,000 or less.
5. Store eligible students.
6. Rank students by aggregate marks in descending order.
7. If aggregate marks are equal, give priority to higher attendance, then lower family income.
8. Display the eligible students and their ranks.
9. Stop.

## 3. Flowchart


          +---------+
          |  START  |
          +---------+
               |
               v
     +---------------------+
     | Enter Student       |
     | Details             |
     +---------------------+
               |
               v
     +---------------------+
     | Check Marks,        |
     | Attendance, Income  |
     +---------------------+
               |
               v
     +---------------------+
     | Is Student Eligible?|
     +---------------------+
          /          \
        Yes           No
         |             |
         v             v
 +---------------+  +-------------+
 | Store Student |  |   Reject    |
 +---------------+  |   Student   |
         |          +-------------+
         |             |
         +------ +-----+
                |
                v
     +---------------------+
     | Rank Eligible       |
     | Students            |
     +---------------------+
               |
               v
     +---------------------+
     | Display Scholarship |
     | Ranking             |
     +---------------------+
               |
               v
          +---------+
          |  STOP   |
          +---------+


## 4. Python Source Code

```
students = []n = int(input("Enter number of students: "))for i in range(n):    print("\nEnter details of student", i + 1)    name = input("Enter name: ")    marks = float(input("Enter aggregate marks: "))    m1 = float(input("Enter subject 1 marks: "))    m2 = float(input("Enter subject 2 marks: "))    m3 = float(input("Enter subject 3 marks: "))    attendance = float(input("Enter attendance percentage: "))    income = float(input("Enter annual family income: "))    if (marks >= 75 and m1 >= 40 and m2 >= 40            and m3 >= 40 and attendance >= 75            and income <= 200000):        students.append([name, marks, attendance, income])        print("Eligible for scholarship")    else:        print("Not eligible for scholarship")# Ranking and tie-breakingstudents.sort(key=lambda s: (-s[1], -s[2], s[3]))print("\n--- Scholarship Ranking ---")if len(students) == 0:    print("No eligible students")else:    for rank, student in enumerate(students, start=1):
```

## 5. Sample Input

```
Enter number of students: 2

Enter details of student 1
Enter name: Ravi
Enter aggregate marks: 85
Enter subject 1 marks: 80
Enter subject 2 marks: 90
Enter subject 3 marks: 85
Enter attendance percentage: 90
Enter annual family income: 150000

Enter details of student 2
Enter name: Sita
Enter aggregate marks: 92
Enter subject 1 marks: 90
Enter subject 2 marks: 95
Enter subject 3 marks: 91
Enter attendance percentage: 95
Enter annual family income: 100000
```

## 6. Sample Output

```
Eligible for scholarship
Eligible for scholarship

--- Scholarship Ranking ---

Rank: 1
Name: Sita
Aggregate Marks: 92.0
Attendance: 95.0
Family Income: 100000.0

Rank: 2
Name: Ravi
Aggregate Marks: 85.0
Attendance: 90.0
Family Income: 150000.0
```

## 7. Result

The program checks scholarship eligibility and ranks eligible students according to aggregate marks. If aggregate marks are equal, higher attendance gets priority, followed by lower family income.

Note: The eligibility limits and tie-breaking rules used here are example rules. A university can change them according to its official scholarship policy.
