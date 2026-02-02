

#**************************************************VARIABLES************************************************************************




# #Variables are used to store data values.
# #In Python, we do not need to declare variables explicitly.
# #A variable is created the moment you first assign a value to it.
# x=5
# y="Hello,Python!"
# print("The value of x is:",x)
# print("The value of y is:",y)
# #You can also assign multiple values to multiple variables in one line:
# a,b,c=10,20,"Python" #Multiple assignment
# print(a)
# print(b)
# print(c)
# #You can also assign the same value to multiple variables in one line:
# m=n=p=50
# print(m)
# print(n)
# print(p)
# #Variable names can be of any length and can consist of letters, digits and underscores.
# #However, they must start with a letter or an underscore.
# _var1=100
# var_2=200
# var3_name="Variable 3"  
# print(_var1)
# print(var_2)
# print(var3_name)
# #Variable names are case-sensitive.
# Var=10

# var=80
# print(Var)
# print(var)


#***********************************************************Revision**********************************************






#A variable is created the moment you first assign a value to it.
# Variables do not need to declare with particular type , and can even change type after they have been set.
x=4 
x="Akash"
print(x)
#If you want to specify the data type of a variable, this can be done with casting.
x= str(4)
y=int(4)
z=float(4)
print(x)
print(y)
print(z)
print(type(x),type(y),type(z))
# Python is case sensitive which means that V and v are two different variables.
a=9 ; A=90
print(a)
print(A)

######RULES FOR DECLARING A VARIABLE IN PYTHON:

#1.A variable name must start with a letter(A-z) or underscore(_)
#2. A variable name can not start with a number (0-9)
#3. A variable name can only contain alpha-numeric characters and underscores (A-z,0-9,_)
#4. Variable names are case-sensitive (age, Age and AGE are three different variables)
#5. A variable name can not be a reserved keyword.
# Multiwords Variable names:
#There are several ways to declare multiword variable names:
#1. CAMEL CASE: Each word, exceppt the first, starts with a capital letter.
myVariableName="Ram"
print(myVariableName)
#2.PASCAL CASE: Each word starts with a capital letter.
MyVariableName="Shyam"
print(MyVariableName)
#3.SNAKE CASE:Each word is seperated by underscore character.
my_variable_name="hari"
print(my_variable_name)

#Many Values to multiple Variables:
a, b, c = 5, "orange", 3.5
print(a,b,c) 
print(a); print(b); print(c)
print(a,end=" "); print(b,end=" "); print(c)
# One Value to multiple Variables:
x=y=z= "56"
print(x,y,z)

# Unpacking a COllection:
fruits = ["apple", "banana", "cherry"]
a,b,c=fruits
print(a,b,c)    #This is called unpacking.
print(fruits)

# Output variables:
x="Akash" ; y="is learning Python" ; z="in 2026"
print(x,y,z)
print(x+y+z) #The output contains no spaces between the each variables
print(x+" "+y+" "+z) #The output contains spaces between the each variables

#With numbers + act as the mathematical operator:
#When you try to combine a string and a number with python + operator you will get an error:
x="Ram" ; y=5
# print(x+y) #This will raise a TypeError
print (x+ str(y))

##### So the best way to output multiple variables in python is to use comma , in the print function.
print(x,y)

# GLOBAL VARIABLE : Variable that is declared outside of a functiona nd thus is in the global scope.
x= "awesome"
def myfunc():
    print("Python is " + x)
myfunc()
def myfunc2():
    x="fantastic"
    print("python is " + x)
myfunc2()    
# Generally inside a function the local variable has priority over the global variable.
#Outside the function the global variable is used.
# If you need to create a global variable inside a function, you can use the global keyword.
def myfunc3():
    global y
    y="great"
    print("python is " + y)
myfunc3()

print("He is such a "+y+" man.") #y was although declared inside the function myfunc3() but becasue of global keyword it is accessible outside the function as well.

# To change the value of a global variable inside a function, use the global keyword.
z="good"
def myfunc4():
    global z
    z="bad"

    
    print("python is " + z)
myfunc4()

print(z)


##NOTE : BY default --> Print() function takes last argument by default end='\n' (new line character)
# So every print statement is printed in a new line.
# You can change this behavior by using end parameter of print function.
# For example:
print("Hello", end=" ")
print("World!")
# In the above example both print statements are printed in the same line because we have changed the default behavior of print function by using end=" " parameter.
#Positional and Keyword Arguments in print function:
print("Hello", "World", sep="--") #Here we have used sep parameter to change the default behavior of print function.
print("Hello", "World", end="***\n") #Here we have used end which adds *** at the end of the print statement instead of new line character.





 


