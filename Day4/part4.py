stock = 50
customer = 0

while stock >= 3:
    customer += 1
    stock -= 3
    print(f"Customer {customer} served, Ice creams left: {stock}")

print(f"No more ice creams! Customers served: {customer}")
