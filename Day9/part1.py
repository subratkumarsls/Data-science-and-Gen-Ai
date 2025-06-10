student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 88,
    "Diana": 95
}

max_name = max(student_scores, key=student_scores.get)
print(max_name, student_scores[max_name])