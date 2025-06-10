numbers = {
    "a": 10,
    "b": 15,
    "c": 5,
    "d": 20
}
threshold = 12
filtered = {k: v for k, v in numbers.items() if v <= threshold}
print(filtered)