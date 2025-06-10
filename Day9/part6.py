employees = {
    "emp1": {"name": "John", "department": "HR"},
    "emp2": {"name": "Emma", "department": "IT"},
    "emp3": {"name": "Harry", "department": "Finance"}
}
for emp in employees.values():
    print(f"{emp['name']} works in {emp['department']} department.")