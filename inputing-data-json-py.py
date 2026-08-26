import json

students = [
    {
        "id": 1,
        "name": "Sarthak",
        "marks": 92
    },
    {
        "id": 2,
        "name": "Rahul",
        "marks": 85
    }
]

with open("students.json", "w") as file:
    json.dump(students, file)