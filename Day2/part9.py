call_rate = 0.80
day1_minutes = 50
day2_minutes = 30
total_cost = call_rate * (day1_minutes + day2_minutes)
print(f"Total Cost: {total_cost}")
print(f"Is total cost == 64.0 ? {total_cost == 64.0}")