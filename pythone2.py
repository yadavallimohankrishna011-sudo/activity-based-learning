# Progressive Water Tariff Analysis

households = [100, 250, 400, 600]

fixed_fee = 50
penalty = 100

for units in households:

    if units <= 100:
        bill = units * 2
    elif units <= 300:
        bill = (100 * 2) + (units - 100) * 3
    else:
        bill = (100 * 2) + (200 * 3) + (units - 300) * 5

    bill = bill + fixed_fee

    if units > 400:
        bill = bill + penalty

    print("Water Consumption:", units, "units")
    print("Total Bill: Rs.", bill)

    if units > 400:
        print("Excessive Usage")
    else:
        print("Normal Usage")

    print("-------------------")