#--------------------Python Iterators
#An iterator is an object that contains a countable number of values.
# Iterable = something you can loop over (like a list, string, etc.) --> If you can use it in a for loop → it’s an iterable
# Iterator = the thing that gives you values one by one

# Iterable = Box of chocolates
# Iterator = The hand that takes out one chocolate at a time
# | Feature            | Iterable | Iterator            |
# | ------------------ | -------- | ------------------- |
# | Has values         | ✅ Yes    | ❌ No (gives values) |
# | Remembers position | ❌ No     | ✅ Yes               |
# | `iter()` works     | ✅ Yes    | ❌ Already iterator  |
# | `next()` works     | ❌ No     | ✅ Yes               |

# For example ; name ="Akash"
#               it= iter(name) # Character by character access is via iterator
#         print(next(it)) #A
#         print(next(it)) #k
#         print(next(it)) #a

#Iterable holds data.
#Iterator delivers data one-by-one.

#The for loop actually creates an iterator object and executes the next() method for each loop.

mystr = "banana"
myit= iter(mystr)
print(next(myit)) #b
print(next(myit)) #a

myTuple = ("apple", "banana", "cherry")
for x in myTuple:
    print(x)

#--------------------------------------Python Modules
# 
# A module is a file which contains set of functions or code that you want to reuse in your application or in another file
# FILE1: math_ops.py  
#                      def add(a, b):
#                          return a + b
                     
#                      def sub(a, b):
#                          return a - b

# FILE2: main.py
#                    import math_ops
                   
#                    print(math_ops.add(5, 3))
#                    print(math_ops.sub(10, 4))

# Way to import a module:
# 1. import module_name
#             import math_ops
#             math_ops.add(2, 3)

# 2. from module_name import function_name 
#                          from math_ops import add
#                          add(2, 3)

#3.Import with alias
#                          import math_ops as mo
#                          mo.add(2, 3)

# The dir() lists all function names in a module

# ---------------------------------Pyhton Date and Time



# ----------------------------------Python math module

# min() , max() , abs() , pow() , round() , floor() , ceil() , sqrt() , log() , log10() , exp() , sin() , cos() , tan() etc.
# min() , max() --> returns the minimum and maximum of a set of values.
# abs() --> returns the absolute value of a number.
# pow() --> returns the value of x to the power of y.
# round() --> rounds a number to a specified number of decimal places.

#-----------------------------JSON in Python
#JSON = JavaScript Object Notation
#JSON is a syntax for storing and exchanging data.
#JSON is a text format that is completely language independent but uses conventions that are familiar to programmers of the C-family of languages, including Python.
#JSON is often used when data is sent from a server to a web page.

# Python has a built-in package called json, which can be used to work with JSON data.

import json
# Convert Python object to JSON string
data = {"name": "John", "age": 30, "city": "New York"}
json_string = json.dumps(data)
print(json_string) #{"name": "John", "age": 30, "city": "New York"}
# Convert JSON string to Python object
json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)
print(data) #{'name': 'John', 'age': 30, 'city': 'New York'}

#-------------------------------------RegEx in python
#RegEx = Regular Expression
#A regular expression is a sequence of characters that defines a search pattern.
#RegEx can be used to check if a string contains the specified search pattern.

#Python has a built-in package called re, which can be used to work with regular expressions.
import re
txt = "The raining in Spain stays mainly in the plain."
x=re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")

# RegEx Functions:
# findall() , search() , split() , sub() , match() , etc.
# Returns list of all matches , search for a match , split the string at each match , replace matches with a string , etc.
#Metacharacters:
# . ^ $ * + ? { } [ ] \ | ( )
# . --> Any character except newline
# ^ --> Starts with
# $ --> Ends with
# * --> Zero or more occurrences
# + --> One or more occurrences
# ? --> Zero or one occurrence
# { } --> Exactly the specified number of occurrences
# [ ] --> A set of characters
# \ --> Escape special characters
# | --> Either or
# ( ) --> Capture and group

#Sets
#[arn] --> a , r or n
#[a-n] --> any character from a to n
#[^arn] --> any character except a , r or n
#[0-9] --> any digit from 0 to 9
#[^0-9] --> any character except a digit from 0 to 9


# ---------------------------------------Python PIP

#PIP = Preferred Installer Program
#PIP is a package manager for Python packages, or modules if you like.
#PIP is used to install and manage software packages written in Python.
#To install a package using PIP, you can use the following command in your terminal or command prompt:
# pip install <package_name>









 
