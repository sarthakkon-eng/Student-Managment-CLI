import json
#f = open("students.json", "r") is how we use read files

with open("students.json", "r") as f:
    students = json.load(f)

print(students)