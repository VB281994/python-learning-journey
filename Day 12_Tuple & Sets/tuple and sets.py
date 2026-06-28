#Tuple - Data that should not change. it is like lists (DOB)
#set - Store unique values (no duplicates)

#Accessing tuple value
days = ("Monday","Tuesday","Wednesday")
print(days[1])

#Loops through a tuple
for day in days:
    print(day)

#where do use tuple
screen = (1920, 1080)
connection = ("localhost","root","password123")

#Set - A store only unique values. it automatically remove duplicates.
fruits = {
    "Apple",
    "Banana",
    "Apple",
    "Mango"
}
print(fruits)    #removed apple from sets output = {'Mango', 'Apple', 'Banana'}

fruits.add("Orange")    #Adding data
print(fruits)

fruits.remove("Apple")
print(fruits)