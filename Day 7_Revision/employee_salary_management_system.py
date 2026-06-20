name = input("Enter Name: ")
salary = int(input("Enter Salary: "))
expenses = int(input("Enter Expenses: "))

saving = salary - expenses

if saving >= 50000:
    print("Excellent")
elif saving >= 20000:
    print("Good")
else:
    print("Need Improvement")