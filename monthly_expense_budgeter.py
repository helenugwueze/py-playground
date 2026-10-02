categories = ("Food", "Rent", "Utilities")
expenses = ["Food", "Utilities", "Luxury", "Food"]
total_spent = 0

for item in expenses:
    if item == "Rent":
        total_spent = total_spent + 500
    elif item == "Food":
        total_spent = total_spent + 50
    elif item == "Utilities":
        total_spent = total_spent + 100
    else:
        total_spent = total_spent + 200

print(total_spent)
