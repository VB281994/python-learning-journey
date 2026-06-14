salary = int(input("Enter Salary: "))
rent = int(input("Enter Rent: "))
food = int(input("Enter Food Cost: "))
travel = int(input("Enter Travel Cost: "))

total_expenses = rent + food + travel
remaining_balance = salary - total_expenses

print("Total Expenses:", total_expenses)
print("Remaining Balace:", remaining_balance)