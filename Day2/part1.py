# Day 1
itemA_price = 100
itemB_price = 200
quantityA1 = 2
quantityB1 = 1
print(f"Day 1 total cart value is {itemA_price*quantityA1+itemB_price*quantityB1}")
# Day 2
quantityA2 = 4
quantityB2 = 2
print(f"Day 2 total cart value is {itemA_price*quantityA2+itemB_price*quantityB2}")
print(f"Is Day 2 total >= Day 1 total?{not(itemA_price*quantityA1+itemB_price*quantityB1 >= itemA_price*quantityA2+itemB_price*quantityB2)}")