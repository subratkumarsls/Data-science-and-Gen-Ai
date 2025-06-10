amounts = [700, 4500, 1200]
for i in range(3):
    spent = amounts[i]
    if spent > 5000:
        discount = "30%"
    elif spent > 1000:
        discount = "20%"
    elif spent > 500:
        discount = "10%"
    else:
        discount = "no"
    print(f"Customer {i+1} gets {discount} discount.")
