import json
#f = open("students.json", "r") is how we use read files

with open("students.json", "r") as f:
    students = json.load(f)

def add_student():
    name = input("Enter student name: ")
    stu_id = int(input("Enter student id: "))
    marks = int(input("Enter student marks: "))
    stu_info = {
        "id": stu_id,
        "name": name,
        "marks": marks
    }
    students.append(stu_info)
    with open("students.json", "w") as f:
        json.dump(students, f)
def Search_student():
    pass

def update_student():
    pass

def Delete_student():
    pass

print("Welcome to Student Management System")
print("Menu:")
print("1. Add Student")
print("2. Search Student")
print("3. Update Student")
print("4. Delete Student")
x = int(input("Enter your choice: "))
if x == 1:
    add_student()
elif x == 2:
    Search_student()
elif x == 3:
    update_student()
elif x == 4:
    Delete_student()