attendance_list=[]
def mark_present(student_name: str):
    if student_name not in attendance_list:
        attendance_list.append(student_name)
        print(f"{student_name} has been marked as present.")
    else:
        print(f"{student_name} is already marked as present.")
def remove_student(student_name: str):
    if student_name in attendance_list:
        attendance_list.remove(student_name)
        print(f"{student_name} has been removed from the attendance list.")
    else:
        print(f"{student_name} is not in the attendance list.")
def is_present(student_name: str) -> bool:
    return student_name in attendance_list
def display_attendance():
    if attendance_list:
        print("Present students:")
        for student in attendance_list:
            print(f"- {student}")
    else:
        print("No students are currently marked as present.")
n=int(input("enter the initial no. of students in the list"))

add=input("Add Name")
mark_present(add)

rem=input("Remove Name")
remove_student(rem)

print("Check if Ram is present: ")
print(is_present("Ram"))

display_attendance()
