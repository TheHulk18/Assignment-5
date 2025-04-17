student_marks = {
    "Sarthak": 85,
    "Pratik": 90,
    "Dhanashree": 78,
    "Vaishnavi": 92,
    "Nimisha": 89
}


student_name = input("Enter the student's name: ")


if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Sorry, no records found for {student_name}.")