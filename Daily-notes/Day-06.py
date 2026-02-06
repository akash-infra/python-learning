#Today we learn Taking Inputs from User and Type Casting

# Taking Input from User
# In Python, we can take input from the user using the input() function.
#The input  function always returns a string value.
name = input("Enter your name: ")
print("Your name is:",name)
age = input("Enter your age:")  # Input function always takes input as string
print("Your age is:",age)
#If we want to take numerical input, we need to convert the string to an integer or float.
print ("Your current age is:",int(age))
height=input("Enter your heights inmeters:")
print("Your height is:",float(height),"metres")
# Type Casting
# Type casting is the process of converting one data type to another.
# In Python, we can use the following functions for type casting:
# int() - converts a value to an integer
# float() - converts a value to a float
# str() - converts a value to a string
# Example:
str1="100" ; str2 ="250.5"
print("str1+str2 =",str1+str2)  #This will print 100250.5 because both str1 and str2 are strings.
#To perform arithmetic operations we need to convert them to integers or floats.
print("After converting to integers :",float(str1)+float(str2))
#After converting to intgers : 350.5
print("After converting to floats:",float(str1)+float(str2))

#After converting to floats: 350.5
#Similarly, we can convert other data types as well.
#For example:
a=10
b=20.5

print("a as float:",float(a))

print("b as int:",int(b))

#Output:
# a as float: 10.0
# b as int: 20
#We can also convert boolean values to integers and floats.
c=True
d=False
print("c is Bollean but afeter converting to int:",int(c))
print("d is Bollean but afeter converting to float:",float(d))
dictionary={"name":"Alice", "age":30}
print("Disctionary to string",str(dictionary))
#Now dictionary is converted to string.
#Output:
# c is Bollean but afeter converting to int: 1
# d is Bollean but afeter converting to float: 0.0
# Disctionary to string {'name': 'Alice', 'age': 30}
#Note: Some type conversions may result in errors if the conversion is not possible.
#For example, trying to convert a string that does not represent a number to an integer will raise a ValueError.
#Example:
invalid_str = "Hello"
print(int(invalid_str))  #This will raise a ValueError
   
# ValueError: invalid literal for int() with base 10: 'Hello'
#Similarly, trying to convert a complex number to an integer or float will raise a TypeError.
#Example:
complex_num = 2 + 3j
print(int(complex_num))  #This will raise a TypeError
# TypeError: can't convert complex to int
#print(float(complex_num))  #This will also raise a TypeError
# TypeError: can't convert complex to float
#Therefore, it is important to ensure that the value being converted is compatible with the target data type.
#That's all for today's lesson.




