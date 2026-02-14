#**************************************** Python Dictionories ****************************************************

#  stores Key-Value pair 
# Dic are ordered , changeable , no duplicate keys allowed.
# Uses Curly {} braces
dict1={"car":"BMW","bike":"Ducati","plane":"Airbus"}
print(dict1)
print(type(dict1))
print(len(dict1))
#The dict() Constructor
dict2=dict(day="Monday",month="January",year=2026)
print(dict2)

# Accessing Items
print(dict1["car"])
# get() : Another way to access value of a key  
print(dict1.get("bike"))

# Keys()  : This method returns a list of all the keys in the dictionary
print(dict1.keys())

# Values() : This method returns a list of all the values in the dictionary
print(dict1.values())

# Items()  : This method returns each item in a dictionary as a tuple in a list
print(dict1.items())
#---------------------------------Adding , Updating , Removing Elements

# Adding is done with key value assignment
dict1["train"]="Maharaja Express"
print(dict1)

# update()  : To update existing key value pair
dict1.update({"car":"Audi"})
print(dict1)
# remove elements : pop() , popitem() , del , clear()
# pop() : removes the item with the specified key name
dict1.pop("bike")
print(dict1)
# popitem() : removes the last inserted item
dict1.popitem()
print(dict1)
# del : removes the item with the specified key name
del dict1["plane"]
print(dict1)
# clear() : empties the dictionary
dict1.clear()
print(dict1)
# del : deletes the dictionary completely
del dict1
#print(dict1)  # This will cause an error because dict1 no longer exists

# -----------------------------------Copying a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# copy()  : Make a copy of a dictionary with the copy() method
dict3={"name":"Akash","age":25}
dict4=dict3.copy()
print("dict4:",dict4)
# dict()  : Another way to make a copy is to use the dict() function
dict5=dict(dict3)
print("dict5:",dict5)
