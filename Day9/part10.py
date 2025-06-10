students = {
    "Alice": ["Math", "Science"],
    "Bob": ["English"],
    "Charlie": ["History", "Math"]
}
new_subject = "Physical Education"
for subjects in students.values():
    subjects.append(new_subject)
print(students)