#Colby king module 8 student program#
import json

# Load JSON Data
def load_students(filename="student_list.json"):
    with open(filename, "r") as file:
        students = json.load(file)
    return students

# Print Student List
def print_students(students, message):
    print("\n" + message)
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Save JSON Data
def save_students(students, filename="student_list.json"):
    with open(filename, "w") as file:
        json.dump(students, file, indent=4)
    print("\nThe student.json file has been updated.")

# Main Program Execution
students = load_students()
print_students(students, "Original Student List:")

# Append New Student Data
new_student = {
    "F_Name": "Colby",
    "L_Name": "King",
    "Student_ID": 99999,
    "Email": "colby.king@gmail.com"
}

students.append(new_student)
print_students(students, "Updated Student List with New Entry:")
save_students(students)
