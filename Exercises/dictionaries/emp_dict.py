#*****************  1.Create an empty dictionary. ****************************************

my_dict1=dict()
my_dict2={}
print(my_dict1)
print(my_dict2)

# Both are same ways to create an empty dictionary
# dict() ---> Is a Construtor method --> Usualy used to convert the other data types into dict
# {}     ---> Is a Literal method ---> Shorter and real industrial Use. Widely used in Projects 

# ****************** 2. Add  a new key value pair ******************************************

new_dict=my_dict1.update({"Village":"Songra"})
print(new_dict)  # ---> Return None because .update() modifies dict in-place and returns nothing
my_dict1["PIN"]=2024
print(my_dict1)


#************************* 3.Update Value of an existing key *************************************

temp_dict={
    "Car":"XUV700",
    "Brand":"Mahindra",
    "Model": 2024
}
print(temp_dict)
temp_dict["Model"]=2022
print(temp_dict)

# temp_dict.get("Model")=2021  -- 
# print(temp_dict)             -- error because .get() is a function which returns value only.

# dict[key]  ---> Read + Update
# dict.get(key)  ---> Safe Read Only

#************************************ 4. Delete a Key from dictionary ****************************
#temp_dict.clear()  -----> Clears the dictionary items
print(temp_dict)
temp_dict.pop("Model")
#                          # popitem() --->Removes the random item(Py 3.7)
print(temp_dict)

del temp_dict["Brand"]
print(temp_dict)

#*************************************5. Check if a key exists *************************************

prod_dict={
    "Tomato":"1KG",
    "Potato":"2KG",
    "CokeCola":4,

}

#if "Tomato" in prod_dict.keys():
if "Tomato" in prod_dict:
    print("Yes!Tomato are written")

#******************************************* 6. Get Value Safely without Key Error ******************

print(prod_dict.get("Tomato"))
print(prod_dict.get("Cucumber"))
# print(prod_dict["Garlic"]) ------->KeyError: 'Garlic'

# dict[key] --->Gives "Keyerror" if Key is missing
# .get(key) ---> "None" if Key is missing


#********************************************* 7. Iterate Over Keys  and values and key-value pairs********************************

student = {
    "name": "Akash",
    "age": 22,
    "course": "MCA",
    "city": "Ghaziabad"
}

for x in student:
    print(x,student[x])
   # print(x)

for x,y in student.items():
    print(x,y,sep="-")

for x in student.keys():
    print(x)

for y in student.values():
    print(y)

#****************************************** 8. Merge Two Dictionaries *******************************
print("______________________________________________________________________")

# for x in prod_dict:
#     student[x]=prod_dict[x]
# print(student)

#merged_dict=student.update(prod_dict)
#print(merged_dict) #--> Error/None becuase .update is in-place modification and returns nothing
student.update(prod_dict)
# print(student.update(prod_dict)) ---> Prints None
print(student)



