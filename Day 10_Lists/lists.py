#normal list
fruites = ["Apple", "Banana", "Mango"]
print(fruites)
print(fruites[0])  #for printing specific index
print(fruites[-1]) #Negative indexing (-1=last item, -2=second last item)
fruites[1] = "Orange"   #changing value of "Banana"
print(fruites)
fruites.append("Mango")   #add new item at the end
print(fruites)
fruites.remove("Mango")  #Remove end item from list
print(fruites)
print(len(fruites))  #To find lenghth of the lists

#Loops through a list
for fruit in fruites:
    print(fruit)

#Real life example
cart = []
cart.append("Protein Powder")
cart.append("Oats")
cart.append("Milk")
print(cart)

#insert() - add value at specific position
cart.insert(1, "Creatine")   # (index, object or item)
print(cart)

#pop() - remove value at specific position
cart.pop()   #remove item the last item
print(cart)
cart.pop(1)  #remove specific position
print(cart)

#sort() - arrange data - ascending order
numbers = [40, 10, 50, 20, 50]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)  #Descending order
print(numbers)
print(numbers.count(50))  #count how many times item appear
#indexing - find items position
print(numbers.index(20))
