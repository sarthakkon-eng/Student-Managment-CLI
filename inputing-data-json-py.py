import json

students = [
    {"id": 1, "name": "Sarthak", "marks": 92}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)