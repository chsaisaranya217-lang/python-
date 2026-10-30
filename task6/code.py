n = int(input("Enter number of passengers: "))

total = 0

for i in range(n):
    age = int(input("Enter age: "))
    distance = float(input("Enter distance: "))

    print("1. Sleeper")
    print("2. AC")
    choice = int(input("Enter class: "))

    if choice == 1:
        rate = 2
    else:
        rate = 4

    fare = distance * rate

    if age >= 60:
        fare = fare - (fare * 0.10)

    fare = fare + 20

    print("Passenger Fare:", fare)
    total = total + fare

print("Total Railway Fare:", total)
