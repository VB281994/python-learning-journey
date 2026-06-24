#Multiple Argument
# def employee(name, salary):
#     print("Employee", name)
#     print("Salary", salary)

# employee("Vasant", 32)

#Return value function
# def add():
#     result = 10 + 5
#     print(result)
#     return result
# add()

#return with parameter
# def less(num1, num2):
#     result = num1 - num2
#     print(result)
#     return result

# less(10,20)

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

result = calculate_bmi(78, 1.73)
print(result)