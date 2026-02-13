# ***************************** Python Tuples ******************************************************************

# An Ordered Collection
# Immutable( can not remove , delete , add elements after crreation)
# Allows duplicate values , can store multiple datat types

# IN Python , ()  :---> Does not create tuple and it does not mean its a tuple.
# () ;--> Is used for three thing in python; 1.Expression Grouping 2.Function calls 3.Tuple container(When comma is present)
# Python first identifies the container type: {} , [] , ()
# [] , {} decides List and Dictionary but () does not decides it a tuple , however "," does this
# , creates the tuple | comma is the tuple operator | Parenthessis becom optional.
#Tuples are stored in contiguos Memory and never changes
# Funcction Arguments are stored as tuple
# It protects data from accidental modification
t=(1,2,3,4,)
print(t)

x=3,4,5,6,7,8,  # Tuple packing

t1=(5)     #----->Is not a tuple
t2=(5,)    #------> Is a tuple

# Since , tuples  are indexes so they can have duplicate vaalues.

#---------------------------1.Accessing tuples
# Same as Lists

print(t[0]) ; print(t[3])

print(t[2:4])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#-----------------------------2.Updating the tuple

#As tuple are immutable objects thats why you can not directly remove, add,delete element
# COnvert tuple-->List , change list , then List---tuple
x=("Ram","Shyam","radha")
y=list(x)
y.append("Sita")
x=tuple(y)
print(y)

#HOWEVER , YOU CAN A TUPLE INTO ANOTHER TUPLE
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#-----------------------------------3.Unpacking Tuple

fruits=("mango","apple" ,"banana")
(green,yellow,red)=fruits
print(green)
print(yellow)
print(red)


#**********************************************Python Sets *****************************************************************

# *Unordered , Mutable , Stores Unique element Only , Uses Curly {} braces
x={}
print(type(x))   # Not a set
# {}  ---> Not create a set . Because python reserved {} for dictionaries
# Bracket decided Container and comma seperates element
s=set()  # is a empty set

# Sets uses HAshes thats why duplicate hashes are ignored.

# Inside Set Mutable Objects are not allowed , immutable are allowed

#----------As set are unordered hence indexing  does not work here.No Slicing , No indexing
#--------------------Adding , Removing Elements

 # add()  : To add one item in set
myset={"car","bus","truck"}
myset.add("ferrari")
print(myset)

# update()  : Add any object in a set
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#remove()  :If the item to remove does not exist then remove will through an error
#discard() : if the item to remove does not exist then discard() will NOT thrugh erro
#clear()   : Empty the set completely
#del   : This keyword deleted set entirely ,set does not exist anymore

# Set operations:
a={1,2,3}   
b={3,4,5}
print(a|b) #{1,2,3,4,5}
print(a&b) #{3}
print(a-b) #{1,2}
print(a^b) #{1,2,4,5}

#NOTE: frozenset---->immutable