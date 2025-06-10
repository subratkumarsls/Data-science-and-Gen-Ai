inventory = {
    "pen": 10,
    "pencil": 0,
    "eraser": 5,
    "notebook": 0
}
cleaned_inventory = {item: qty for item, qty in inventory.items() if qty != 0}
print(cleaned_inventory)