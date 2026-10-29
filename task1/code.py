
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Enter name: ")
    marks = float(input("Enter aggregate marks: "))

    m1 = float(input("Enter subject 1 marks: "))
    m2 = float(input("Enter subject 2 marks: "))
    m3 = float(input("Enter subject 3 marks: "))

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    if (marks >= 75 and m1 >= 40 and m2 >= 40
            and m3 >= 40 and attendance >= 75
            and income <= 200000):

        students.append([name, marks, attendance, income])
        print("Eligible for scholarship")
    else:
        print("Not eligible for scholarship")


students.sort(key=lambda s: (-s[1], -s[2], s[3]))

print("\n--- Scholarship Ranking ---")

if len(students) == 0:
    print("No eligible students")
else:
    for rank, student in enumerate(students, start=1):
        print("Rank:", rank)
        print("Name:", student[0])
        print("Aggregate Marks:", student[1])
        print("Attendance:", student[2])
        print("Family Income:", student[3])
        print()

