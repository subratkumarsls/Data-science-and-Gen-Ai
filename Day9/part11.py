dict1 = {'x': 1, 'y': 2, 'z': 3}
dict2 = {'w': 10, 'x': 11, 'y': 22}
common_keys = list(dict1.keys() & dict2.keys())
print("Common keys:", common_keys)