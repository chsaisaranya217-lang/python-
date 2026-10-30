Problem Statement: Calculate railway ticket fares for multiple passengers based on distance, travel class, age concessions, reservation fees, and cancellation charges.

Algorithm:
1. Start.
2. Enter passenger details.
3. Enter distance and travel class.
4. Calculate basic fare.
5. Apply age-based concession.
6. Add reservation fee.
7. Calculate final fare.
8. Display ticket details.
9. Stop.
Flowchart:
          START
            |
            v
   Enter number of passengers
            |
            v
    Enter passenger details
   (Name, Age, Distance)
            |
            v
     Select travel class
      (Sleeper / AC)
            |
            v
   Calculate distance-based fare
            |
            v
    Apply age concession
            |
            v
     Add reservation fee
            |
            v
      Is ticket cancelled?
          /       \
        Yes        No
         |          |
         v          |
  Calculate penalty |
         |          |
         v          v
     Calculate final fare
            |
            v
     Display passenger fare
            |
            v
    More passengers?
        /       \
      Yes        No
       |          |
       v          v
  Repeat       Display total fare
                   |
                   v
                  STOP






slideshare.net


Python Source Code:
n = int(input("Enter number of passengers: "))total = 0for i in range(n):    age = int(input("Enter age: "))    distance = float(input("Enter distance: "))    print("1. Sleeper")    print("2. AC")    choice = int(input("Enter class: "))    if choice == 1:        rate = 2    else:        rate = 4    fare = distance * rate    if age >= 60:        fare = fare - (fare * 0.10)    fare = fare + 20    print("Passenger Fare:", fare)    total = total + fareprint("Total Railway Fare:", total)



Sample Input:
Enter number of passengers: 2
Enter age: 65
Enter distance: 100
Enter class: 1
Enter age: 25
Enter distance: 100
Enter class: 2


Output:
Passenger Fare: 200.0
Passenger Fare: 420.0
Total Railway Fare: 62.0
