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
    stu_id = int(input("Enter student id to search: "))
    for i in students:
        if i["id"] == stu_id:
            print("Student found: ",i)
        else:
            continue          

def update_student():
    stu_id = int(input("Enter student id to update: "))
    for i in students:
        if i["id"] == stu_id:
            name = input("Enter new name: ")
            marks = int(input("Enter new marks: "))
            i["name"] = name
            i["marks"] = marks
            with open("students.json", "w") as f:
                json.dump(students, f)
            print("Student updated successfully")
            return
    print("Student not found")

def Delete_student():
    stu_id = int(input("Enter student id to delete: "))
    for i in students:
        if i["id"] == stu_id:
            students.remove(i)
            with open("students.json", "w") as f:
                json.dump(students, f)
            print("Student deleted successfully")
            return
    print("Student not found")

print("===== Student Management System =====")
print("")
print("1. Add Student")
print("2. Search Student")
print("3. Update Student")
print("4. Delete Student")

choice = "no"
while choice == "yes":
    x = int(input("Enter your choice: "))
    if x == 1:
        add_student()
    elif x == 2:
        Search_student()
    elif x == 3:
        update_student()
    elif x == 4:
        Delete_student()
    choice = input("Do you want to continue? (yes/no): ")
