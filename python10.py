# Campus Festival Registration and Financial Audit

participants = [
    ("101", 500),
    ("102", 500),
    ("103", 500),
    ("101", 500),
    ("104", 500)
]

sponsorship = 5000
expenses = 3000

seen = []
duplicates = []

total_fees = 0

for id, fee in participants:

    if id in seen:
        duplicates.append(id)
    else:
        seen.append(id)
        total_fees += fee

total_income = total_fees + sponsorship
balance = total_income - expenses

print("Total Participants:", len(seen))
print("Total Registration Fees:", total_fees)
print("Sponsorship Amount:", sponsorship)
print("Total Income:", total_income)
print("Total Expenses:", expenses)
print("Final Balance:", balance)

print("Duplicate Registrations:", duplicates)