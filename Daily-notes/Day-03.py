######################################    DATA TYPES IN PYTHON ###################################################################




#You can also change the type of a variable by assigning a new value
x = "Now I am a string"
print("The new value of x is:", x)
print("The type of variable x is now:", type(x)) # Checking the new data type of variable x
# Summary of common data types in Python:
# int    : Integer numbers (e.g., 1, 2, 3)
# float  : Floating-point numbers (e.g., 1.5, 2.75)
# str    : Strings (e.g., "Hello", 'World')
# bool   : Boolean values (True or False)
# NoneType: Represents the absence of a value (None)
# In the next lesson, we will learn about basic operations with these data types.
list1 = [1, 2, 3, 4, 5] # A list variable 
print("list1:", list1)
tuple1 = (1, 2, 3, 4, 5)
print("tuple1:", tuple1)
set1 = {1, 2, 3, 4, 5}
print("set1:", set1)
dict1 = {"name": "Akash", "age": 25}
print("dict1:", dict1)
#difference between list and tuple is that list is mutable and tuple is immutable
list1[0] = 10
print("Updated list1:", list1)
# tuple1[0] = 10 # This will cause an error because tuples are immutable    
# dict1 is a dictionary which is a collection of key-value pairs
dict1["age"] = 26
print("Updated dict1:", dict1)
# set1 is a collection of unique elements
set1.add(6) 
print("Updated set1:", set1)


#The all data types in Python are:
#1. Numeric Types: int, float, complex
#2. Sequence Types: list, tuple, range
#3. Text Type: str
#4. Set Types: set, frozenset
#5. Mapping Type: dict
#6. Boolean Type: bool
#7. Binary Types: bytes, bytearray, memoryview
# Let's see some examples of Data Types
# Numeric Types
a=10         #int
b=10.5       #float
c=3+4j       #complex
print("The data type of a is:",type(a))
print ("The Data Type of b is:",type(b))
print("Th data type of c is :",type(c))
# Sequence Types::::
#These are used to store multiple items in a single variable
list1=[1,2,3,4,5]   #Lists are mutable,means they can be changed.
tuple1=(1,2,3,4,5)  #Tuples are immutable,means they cannot be changed.
range1=range(1,10)  #range is used to generate a sequence of numbers
print(type(list1))
print(type(tuple1))
print(type(range1))
print("list1:",list1)
print("tuple1:",tuple1)
print("range1",range1)
# The main difference betwen above three is that lists are mutable while tuples and ranges are immutable.
#for example:
list1[0]=10 #Changing the first element of list1
print("Updated list1::",list1)
list1[2]=40
print("Updayed list1:",list1)
#however, we cannot change the elements of tuple1 and range1
tuple1(2)=98 
print(tuple1)

#Text Type::
str1="Hii,I amlearning python."
str2='It is quite efficient nowadays to learn python with AI.'
str3='''And i am enjoying this learning process,honestly.'''
print("The type os sttring str1 is:",type(str1))
print(str1)
print(str2)
print(str3)
#string concatenation
str4 = str1 + " " + str2
print(str4)
#However
a="10" ; b="20"
print(a+b)  #This will print 1020 because both a and b are strings.
#To perform arithmetic operations we need to convert them to integers or floats.
print("After converting to integers :",int(a)+int(b))
print("After converting to floats:",float(a)+float(b))
#Set Types::
set1={1,2,3,4,5}   #Sets are unordered and unindexed collections of unique elements.
frozenset1=frozenset([1,2,3,4,5]) #frozensets are immutable sets.
print("The type of set1 is:",type(set1))
print("The type of frozenset1 is:",type(frozenset1))
print("set1:",set1)
print("frozenset1:",frozenset1)
#Mapping Type::
dict1={"name":"John", "id":102, "department":"CSE"} #Dictionaries are used to store data in key-value pairs.
print("The type of dict1 is:",type(dict1))
print(dict1)
#Boolean Type::
a=True
b=False
print("The type of a is:",type(a))
print("The type of b is:",type(b))
#Binary Types::
# These are used to store binary data.
byte1=b"Hello"
bytearray1=bytearray(5)
memoryview1=memoryview(bytearray1)
print("The type of byte1 is:",type(byte1))
print("The type of bytearray1 is:",type(bytearray1))

print("The type of memoryview1 is:",type(memoryview1))
print("byte1:",byte1)
print("bytearray1:",bytearray1)
print("memoryview1:",memoryview1)

# Type conversion in Python
# Type conversion is the process of converting one data type to another.
# In Python, we can perform type conversion using built-in functions like int(), float(), str
# , list(), tuple(), set(), dict() etc.
# Implicit Type Conversion
# In implicit type conversion, Python automatically converts one data type to another without any user intervention.
# For example:
x=10 # integer
y=6.7 # float
z=x+y # x is implicitly converted to float
print("The value of z is:",z)
print("Type of z is:",type(z))
#How implicit type conversion works:
#1. If one operand is of a higher data type than the other, the lower data type is converted to the higher data type.
#2. The order of data types from lower to higher is: int -> float -> complex
#Explicit Type Conversion
# In explicit type conversion, the user manually converts one data type to another using built-in functions.
a=5.8 #float
b=89 #int
c=8+7j #complex
x=int(a) # converting float to int
y=float(b) # converting int to float
z=complex(b) # converting int to complex
#p=int(c)     #You can not convert complex into another data type directly.
print("The type of x is:",type(x),"and the value is:",x)
print("The type of y is:",type(y),"and the value is:",y)
print("The type of z is:",type(z),"and the value is:",z)

# Random Example of Type Conversion
# Python does not jave random() function like other programming languages to make random numbers but built-in mudule called random that can be used to generate random numbers.
# import random 
# print("Random number between 1 and 10:",random.randint(1,10))

##################### Type Casting   #################################

#Type casting is the process of converting a variable from one data type to another.
#In Python, we can perform type casting using built-in functions like int(), float(), str(), list(), tuple(), set(), dict() etc.
# We can also convert boolean values to integers and vice versa.
a=5 ; b=9.8 ; c="100" ; d="Sharma" ; e=True ; f=False 
print("The integer value of a , b , c , d , e , f are:",int(a), int(b), int(c), "Cannot convert string to int", int(e), int(f))
print("The float value of a , b , c , d , e , f are:",float(a), float(b), float(c), "Cannot convert string to float", float(e), float(f))
print("The string value of a , b , c , d , e , f are:",str(a), str(b), str(c), str(d), str(e), str(f))
#You can ot convert  a non-numeric string to int or float
#For example:
# x=int(d)  #This will cause an error because d is a non-numeric string.
# Now let's see how to convert a list to a tuple and vice versa.
list1=[1,2,3,4,5]
tuple1=(9,8,7,6,5)
dict1={"name":"Akash", "age":2}
print("Dict to List Conversion is:",list(dict1)) #Converting dictionary to list (only keys are converted)
print("Dict to tuple conversion is:",tuple(dict1)) #Converting dictionary to tuple (only keys are converted)
print("List to Tuple Conversion is:",tuple(list1)) #Converting list to tuple
#print("List to Dict Conversion is ",dict(list1)) #This will cause an error because list cannot be converted to dictionary directly.
print("List---->Dict Conversion:"),dict.fromkeys(list1) #Converting list to dictionary using fromkeys() method
print("Tuple to List Conversion is:",list(tuple1)) #Converting tuple to list
print("Tuple to Dict Conversion is:",dict.fromkeys(tuple1)) #Converting tuple to dictionary using fromkeys() method
#You can also convert a set to a list and vice versa.
set1={"aplha","beta","gamma"}
set2={1,2,3,4,5}
print("Set to List Conversion is:",list(set1)) #Converting set to list
print("Set to Tuple Conversion is:",tuple(set2)) #Converting set to tuple
