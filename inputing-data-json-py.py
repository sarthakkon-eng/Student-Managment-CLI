import json

students = [
    {"id": 6, "name": "Skibidi", "marks": 99}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)