weight = float(input("Enter weight: "))
height = float(input("Enter height: "))

bmi = weight / (height ** 2)
print("BMI:", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Healthy Weight")
elif bmi < 30:
    print("Overweight")
else:
    print("obesity")