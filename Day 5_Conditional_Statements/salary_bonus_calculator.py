salary = int(input("Enter Salary: "))

if salary > 50000:
    bonus = 10000
elif salary > 30000:
    bonus = 5000
else:
    bonus = 2000

print("Bonus:", bonus)
