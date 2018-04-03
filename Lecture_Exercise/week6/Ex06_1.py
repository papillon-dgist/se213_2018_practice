students = [
    ('Alice', ['Programming', 'Classic Mechanics']),
    ('Bob', ['Programming', 'Linear Algebra']),
    ('Carol', ['Analytical Mechanics', 'Linear Algebra', 'Programming'])
]
print(students[2])
print(students[2][1])
print(students[2][1][2])

for student in students:
    print('Name :', student[0])
    print('Courses :', student[1])

for student_name, courses in students:
    print('Name :', student_name)
    print('Courses :', courses)