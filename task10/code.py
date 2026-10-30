venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost per participant: "))
transport = float(input("Enter transport cost: "))
certificate = float(input("Enter certificate cost per participant: "))

participants = int(input("Enter number of participants: "))
sponsorship = float(input("Enter sponsorship amount: "))

fixed_cost = venue + equipment + transport

variable_cost = catering + certificate

total_cost = fixed_cost + (variable_cost * participants)

participant_amount = total_cost - sponsorship

shortfall = max(0, total_cost - sponsorship)

if participant_amount > 0:
    contribution = participant_amount / participants
else:
    contribution = 0

break_even = (fixed_cost - sponsorship) / (contribution - variable_cost)

if break_even < 0:
    break_even = 0
else:
    break_even = int(break_even) + 1

print("\n--- EVENT FINANCIAL REPORT ---")

print("Fixed Cost:", fixed_cost)
print("Variable Cost:", variable_cost)
print("Total Expenses:", total_cost)
print("Sponsorship:", sponsorship)
print("Sponsorship Shortfall:", shortfall)
print("Participant Contribution:", contribution)
print("Break-Even Registrations:", break_even)
