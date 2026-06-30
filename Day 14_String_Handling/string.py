# "" or '' - both are valid
#indexing in String
name = "Vasant"
print(name[0])
print(name[-1])   #negative indexing (-1 = last characte, -2 = second last)

#String Slicing
print(name[0 : 3])    # index 0 to 2 (start from 0 and stop before 3)
print(name[2 : 4])

print(len(name))   #length()

name1 = "bhanushali"
print(name1.upper())   #uppercase()
print(name1.lower())   #lowercase()

name2 = "vasant bhanushali"
print(name2.title())   #titlecase()

company = "Google"
print(company.replace("Google", "OpenAI"))  #replace()

email = "vasant.bhanushali@gmail.com"
print(email.find("@"))    #to find the indexing of letter - find()

url = "https://google.com"
print(url.startswith("http"))   #Output = True/False - to check the value match/present or not at start
print(url.endswith(".com"))     #Output = True/False - to check the value match/present or not at end










