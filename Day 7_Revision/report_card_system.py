#School want simple report card system
# 1. Ask student name.
# 2. Ask marks for 3 subjects
# 3. calculate total marks
# 4. calculate average marks
# 5. Decide grade

student_name = input("Enter your name: ")

math = int(input("Enter Math Marks: "))
english = int(input("Enter English Marks: "))
science = int(input("Enter Science Marks: "))

total_marks = math + english + science
average_marks = total_marks / 3

if average_marks >= 90:
    grade = "A"
elif average_marks >= 70:
    grade = "B"
elif average_marks >= 35:
    grade = "C"
else:
    grade = "D"
# if average_marks >= 90:
#     print(student_name, "Grade A")
# elif average_marks >= 70:
#     print(student_name, "Grade B")

print("----------Report Card----------")
print("Student Name:", student_name)
print("Total Marks", total_marks)
print("Average Marks:", average_marks)
print("Grade:", grade)