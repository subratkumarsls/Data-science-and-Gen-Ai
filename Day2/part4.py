total_laptops = 53
container_capacity = 8
containers_filled = total_laptops / container_capacity
remainder = total_laptops % container_capacity
print(f"Containers filled: {containers_filled}")
print(f"Leftover laptops: {remainder}")
print(f"Any leftover? {remainder != 0}")