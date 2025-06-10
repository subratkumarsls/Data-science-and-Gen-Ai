rent_per_day = 200
food_per_day = 150
cost_3_days = 3 * (rent_per_day + food_per_day)
cost_5_days = 5 * (rent_per_day + food_per_day)
print(f"Cost for 3 days: {cost_3_days}")
print(f"Cost for 5 days: {cost_5_days}")
print(f"Is 5-day cost > 3-day cost? {cost_5_days > cost_3_days}")