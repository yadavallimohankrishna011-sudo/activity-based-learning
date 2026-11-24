# Mobile Plan Cost Optimization

plans = [
    ("Plan A", 199, 2, 28),
    ("Plan B", 299, 3, 56),
    ("Plan C", 399, 5, 84)
]

data_needed = 3
validity_needed = 28
budget = 350

best_plan = None
lowest_cost = 9999

for name, price, data, validity in plans:

    if data < data_needed:
        extra_charge = (data_needed - data) * 50
    else:
        extra_charge = 0

    total_cost = price + extra_charge

    if validity >= validity_needed and total_cost <= budget:
        print(name, "Total Cost:", total_cost)

        if total_cost < lowest_cost:
            lowest_cost = total_cost
            best_plan = name

print("-------------------")

if best_plan:
    print("Best Plan:", best_plan)
    print("Minimum Cost: Rs.", lowest_cost)
else:
    print("No eligible plan available")