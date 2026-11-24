# Laboratory Chemical Inventory Validation

chemicals = [
    ("Chemical A", "Acid", 10),
    ("Chemical B", "Base", 5),
    ("Chemical C", "Flammable", 20),
    ("Chemical D", "Acid", 30)
]

max_quantity = 25
invalid = []

for name, category, quantity in chemicals:

    if quantity > max_quantity:
        invalid.append(name + " - Excess Quantity")

    elif category == "Acid":
        print(name, "- Valid Storage")

    elif category == "Base":
        print(name, "- Valid Storage")

    else:
        print(name, "- Valid Storage")

print("\nInvalid Records:")

for item in invalid:
    print(item)