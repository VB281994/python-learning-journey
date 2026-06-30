#List is like shopping bags, Dictionaries is like ID card 
# Dictionaries are like Adhaar Card, Store data in Keys and values 
# Name : Vasant (left side is key and right side is Value)

student = {
    "name" : "Vasant",
    "age" : 32,
    "city" : "Mumbai"
}
print(student)
print(student["name"])   #only specific value

student["city"] = "Pune"  #change the value
print(student)

student["profession"] = "Software Tester"    #adding the new key and value
print(student)

#Loop through a Dictionary
for key in student:
    print(key, ":", student[key])