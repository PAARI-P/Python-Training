n = int(input("Enter number of students: "))

students = {}

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    mark = int(input(f"Enter marks of {name}: "))
    students[name] = mark

highest_mark = max(students.values())

print("\nStudent(s) with highest mark:")
for name, mark in students.items():
    if mark == highest_mark:
        print(f"{name} - {mark}")