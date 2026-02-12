#************************************************ Python Lists *******************************************************************
#____________________________________________________________________________INTRODUCTION______________________________________
#A List stores multiple values in a single variable.
# List are ordered,changeable(replace,add,remove), and allow duplicate values as list items are indexed.
# 
# Square Brackets is used to creat a list.
marks=[10,20,30]

#Python does not stores this as one value
#                      marks ──▶ [ 10 | 20 | 30 ]
#                                 ↑    ↑    ↑
#                               objects in memory
# Each element-->seperate object    , marks---->refrence(adress)
# A LIST STORES REFERENCES TO OBJECTS , NOT RAW VALUES
#A Python list is a object that stores contiguous array of References to seperate python objects  in RAM.
# The list itself does not store actual values,only references,which why lists are mutable and support hetrogeneous data.

#                   marks (id = 1000) --id(marks)
#                  ┌─────────────────────┐
#                  │ 2000 │ 3000 │ 4000  │  ← references
#                  └─────────────────────┘
 #                     │      │      │
 #                     ▼      ▼      ▼
 #                   obj10  obj20  obj30
 #         id(marks[0])  id(marks[1])  id(marks[2])

print(id(marks))          #--------------> id of the list object
print(id(marks[0]))       #}
print(id(marks[1]))       #}  ------>id of element objects---->each will be an integer-object
print(id(marks[2]))       #}
print(id(id(marks[0])))   #]
print(id(id(marks[1])))   #] -------->id of INTEGER returned by id(marks[i])
print(id(id(marks[2])))   #]


#NOTE:1.id() does not give memory adress ,it just gives identity at run time of an object
#     2. id(marks[1])-->integer-object:140718331874008 ---> That integer itself : *is created(or reused),stored in memory,has its own ID
#     3.id(id(marks[i])) → identity of an integer object created by id()  __---->>>MISLEADING
#FINAL ANSWER:id(x) returns an integer object representing the identity of x.
#             When we call id(id(x)), we are inspecting the memory location of that integer object, not the original object.
#             Due to integer caching and reuse in CPython, id(id(x)) values are unreliable for understanding object memory relationships.

#MENTAL MODEL: marks ──▶ ListObject (A)

            # ListObject contains: 
            # ┌────────────────────────┐
            # │ ref ──▶ IntObject(10)  │
            # │ ref ──▶ IntObject(20)  │
            # │ ref ──▶ IntObject(30)  │
            # └────────────────────────┘
            
            # id(IntObject(10)) ──▶ IntObject(140718331874008)
            # id(IntObject(30)) ──▶ IntObject(140718331874648)
            
            # Some id-integers may share memory (cached)

#🚨 Critical:
      # id(x) is NOT a pointer object
      # It is NOT stored inside the object
      # It is NOT something Python objects “contain”
      # It is just an integer value created by CPython for identification.

# WHAT ACTUALLY HAPPENS Internally :: id(marks[1]) :
#                             * marks[1] → gives a reference to the object 20
#                             *CPython takes the address of that object internally
#                             *Converts that address into an integer value----------->|
#                             *Returns that integer as a normal Python int object     |
#THE LIST STORES REFRENCES LIKE THIS:                                                 |
#             marks (ListObject at A)                                                 |
#                                                                                     |
#             A:                                                                      |
#             ┌───────────────────────────┐                                           |
#            ptr │ ref0 │ ref1 │ ref2        │   ← contiguous array                   |
#             └───────────────────────────┘                                           |A new python integer
#                     │                                                               |Whose value happens to equal the object adress
#                                                                                     |marks:
#                     ▼                                                               |  └─▶ C-level pointer ──▶ IntObject(20)
#                IntObject(20)  (somewhere else in memory)                            |id(marks[1]):
#                                                                                     |  └─▶ Python int object (value = address of IntObject(20))
                                                                                #     |
       #🔥 The reference stored in the list is NOT a Python object                    |
       #It is : A C-level pointer                                                      |
       #        Stored in the list’s internal memory                                   |
       #        Invisible to Python code.Not python objects.Can't be accessed by id()  |
       # id() only returns------------------------------------------------------------>|

#SUMMURY -->marks is a list object that contains a contiguous array of C-level references to other Python objects.
#          These references are not Python objects and cannot be inspected directly.
#          The id() function returns a new Python integer whose value corresponds to the memory identity of an object, not a stored reference.


#                      id(marks[1]) is a Python integer object whose VALUE represents the identity of object 20.
#                       It is not a pointer, not a reference, and not an address object stored anywhere inside the list.
# 

#________________________________________________________Operations On Lists___________________________________________

#-----------------------1.Accessing List:

marks=[10,20,30,40,50]
# Accessing by index
print(marks[0])
print(marks[2])

# Negative indexing:
print(marks[-1])
print(marks[-4])

# Accessing using len()
last=marks[len(marks)-1]
print(last)

#Aceesing using loop:
for m in marks:             # Best when index is not needed
    print(m)
#OR
for i in range(len(marks)-1):        # Use when  index matters
    print(marks[i])
# Accessing using while loop:
i=0
while i<len(marks):
    print(marks[i])
    i+=1
# Accessing multiple or only required elements:OR List Slicing
marks[2:4]     # start-index is include and last-index is excluded
marks[:3]
marks[3:]
marks[:]      # Full copy
marks[1::2]     # Aceesing from index1 to last with 2 step
marks[::-1]     #Reversing List

# Accessing with conditions:
for m in marks:
    if m>15:
        print(m)

# Accessing using membership: True or False
print(90 in marks)  #False
print(10 in marks)  #True

# 🔥 Accessing index+Value together:-->Best professional way
for i ,v in enumerate(marks):
    print(i,v)

#----------------------2.Changing List items::
#  when marks[4]=90
#           What Changes->*Refrence at index 4      
#                         *Old object is dereferenced
#                         *New Object reference is stored
# What does not changes:-> id(marks) remains the same.Thats why list are mutable
# Change item value:
thislist=["apple","banana","cherry"]
thislist[1]="pepper"
print(thislist)
#Changing Multiple items using Slicing:
marks=[10,20,30,40,50,60]
marks[1:5]=[99,69]
print(marks)

      #NOTE: Slice assignment replaces the entire slice-block, not element-by-element.
     #       The replacement iterable can be shorter, longer, or equal in length.
#Python removes the entire slice and inserts the new iterable in its place because slice assignment works at the block level,
#  not element-by-element, allowing lists to dynamically grow or shrink.

# The insert() method inserts a new list item ,without replacing any of the existing values at the specified index.
marks=[1,2,3,4,5,6]
marks.insert(3,899)
print(marks)

#--------------------3.Add List items:

#   append() :Used to add single item at the end
#   extend() :Used to add Multiple items(iterable) at the end
#   insert() :Used to add item at specific index.Index out of range-->insert at nearest valid position

marks.append(7)
print(marks)
list=[10,20]
list.extend([30,40])
print(list)
list.extend("Akash")
#list.extend(["Akash","Vikash"]) -->Throughs error as multiple arguments are passed

print(list)
# Here,extend()only takes only ONE argument and that argument must be ITERABLE.
 #list.extend("Akash")  --> Runs effieciently and result will be [10, 20, 30, 40, 'A', 'k', 'a', 's', 'h'] because strings are iterable
#marks.extend(100) --->Error because 100 is not iterable
marks.append("Ram")
print(marks)       #[1, 2, 3, 899, 4, 5, 6, 7, 'Ram']  because list.append(x)-->ADD X AS SINGLE OBJECT NO MATTER WHAT X is.

marks.append([99,88,77]) 
print(marks)          #[1, 2, 3, 899, 4, 5, 6, 7, 'Ram', [99, 88, 77]]

# Creating a new List:
a=[10,20]
b=a+[90,80]
print(b)
print(a)
b.append(34)
print(b)
x=b
print(a)
print(x)
x.append(00)
print(b)
#Adding using Loop:
marks=[]
for i in range(5):
    marks.append(i)

#-------------------------------4.Remove List items:  

# remove() : Remove by VALUE
       #This method removes the specified value.
       # Incase of duplicate items,removes the first occurance.
       # Raises "ValueError" if value is not found
cars=["Mercedez","Bently","Tata"]
cars.remove("Bently")  
print(cars)
nums=[12,34,56,78,12,34,56]
x=nums.remove(34)
print(nums)
print(x)            # remove returns None

# pop() : Remove by INDEX
      # Returns the popped/removed value
      # If index is not given , then it removes last element
pets=["dog","cat","snake","tiger"]
pets.pop(3)
print(pets)
x=pets.pop(1)
print(pets)
print(x)           # Returns cat

# del   : Its a keyword not method
       # Can remove single element by index , slice the list , remove entire list
       #Does not return Nothing
var=[22,33,44,55,66] 
del var[2]  
print(var)
del var[1:3]   
print(var)
del var        #Entire list delet

# clear() : Remove ALL items
        # List object remains same ,only content is removed
# lst=[12,23,344,5467]
# a=lst
# del lst
# print(lst)  # DELETS the variable lst not the list contents
# print(a)     #Againerror becuase a-->lst and lst-->deleted but not the content
# lst.clear()
# print(lst)             # []


#---------------------------------------5.Loop Lists:

#Loop through items:

task=["Read","Play","Music","Work"]
for element in task:
    print(element)

# Loop through index numbers:
for i in range(len(task)-1):
    print(task[i])


# ---------------------------------------6. List Comprehension
    
# Suppose, 
fruits=["apple","banana","Cherry","Kiwi","Mango"]
#Create a new list containing only the fruits with the letter 'a' in the name based on list fruits above
newList=[]
for x in fruits:
    if "a" in x:
        newList.append(x)
print(newList)

# With List comprehension you can do that in one line,

newList=[x for x in fruits if "a" in x]

#Sytax: 
#newlist = [expression "for" item "in" iterable if condition == True]
newList=[m for m in  fruits if m!="apple"]

# ------------------------------------7. Sorting List

# sort() , sorts the list Alphanumerically , Ascending by default.

hereList=[1,98,3,"Akash","Mango","Cat",2]

hereList.sort()
print(hereList)

#To sort the list in Descending Order:

NewList=[3,65,89,1,23,456,7]
NewList.sort(reverse=True)
print(NewList)

# To reverse a List:
# List.reverse()

#----------------------------------8. Copying the List

# You can not directly copy the list like this Liste2=List1 , it just reference the List1

mylist=NewList.copy()
print(mylist)
 #OR
list2=list(mylist)
print(list2)

#----------------------------------9. Joining the List

list3=list2+mylist
print(list3)

#OR

for x in mylist:
    list2.append(x)

    #OR

    # You can also use the "extend" Keyword for this
    

    






        
