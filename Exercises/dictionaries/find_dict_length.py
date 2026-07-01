#9.****************** Find Dictionary Length without Using len()*****************************

student = {
    "name": "Akash",
    "age": 22,
    "course": "MCA",
    "city": "Ghaziabad"
}
length=0
for x in student:
        length+=1
print(length)

#************************* 10. Clear All Items *************************************************

# student.clear()
# print(student)
 # 
# But Without Built-In Functions

# for x in student:
#         student.pop(x)
# print(student)

###### You can not modify the dictionary at the runtime because python loops over keys ######
##~~~~~~~~~~~ Updating existing value → Allowed
## ~~~~~~~~~~~ Adding/removing keys → Not allowed  

## Python Collections list, dict,set generally should NOT change size during iteration. generally should NOT change size during iteration.

## So, We first create a fixed Key list copy to iterate -->and then delete the dict by accessing it with keys

for x in list(student.copy()):
        del student[x]
print(student)

# *********** Difference between del and pop():
 # del --->Removes key-value pair directly.Does NOT retirm the remopved value.GHives error if key is missing

 # pop()   -----> Removes key AND returns its value.Safely handles the missing keys


#******************************** 11. Copy a Dictionary without built in.********************

employee = {
    "name": "Rahul",
    "age": 28,
    "department": "HR"
}

car = {
    "brand": "Toyota",
    "model": "Fortuner",
    "year": 2022
}

# empty dictionary:
emp_dict={}

for x in employee:
        emp_dict[x]=employee[x]
print(emp_dict)  

# employee[x]---> Does x exist in employee-->Yes-->give its value
# empt_dict[x]--->does x exist in empt_dict ---> No-->Assign this key-value(employee[x])




