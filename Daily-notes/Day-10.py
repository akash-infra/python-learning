#********************************************Functions***************************************************************

# Functions are logic written to avoid repetion of logic again and again
#Functions are case seensitive
#It's a good practice to use descriptive names that explains what function does.
#With functions , you arite code once and reuse it.

def farenheit_to_celcious(fahrenheit):
    
    return (fahrenheit-32)*5/9

# Function can send datat back to the code that called them using return statement
#When afunction reaches return statements, it stops executing and sends result back

def get_greetings():
    return "Hello! from akash"
message=get_greetings()
print(message)    #OR print(get_greetings)

# If a function does not have a return statement, it returns None by default.

## PYTHON ARGUMENTS:
#Arguments-->The actual value that is sent to the function when it is called.
#Parametre--->Variable listed inside the parenthesis in the function defination
def my_function(a,b):    # a, b are parameter
    return a*b

my_function(4,8)          # 1,2 are arguments

# By default, a function must be called correct number of expected arguments.

def you_name(fname,lname):
    m="My name is "+fname+" "+lname
    return  m
print("What is your name? ",you_name("Akash","sharma"))

#Default Parametr:
#                If the function is called without passing an argument than it uses the default value.

def my_country(country="India"):
    print("I am from ",country)

my_country("Sweden")
my_country("America")
my_country()
my_country("Newzeland")
my_country("Iran") 

#1.Keyword Arguments:kwargs ------------------------>
#This way , with keyword arguments, the order of the arguments does not matter.

def new_function(animal,name):
    print("I have a ",animal)
    print("My",animal +"'s  name is",name)

new_function(animal="dog",name="Bruno")
new_function(name="Rani", animal="Cow")

#2.Positional Arguments:--------------------------->

# When you call a fuction with arguments without using keywords,they are called positional arguments
# The order matters with positional arguments

#NOTE: You can mix both type arguments but Positional Arguments>Keyword Arguments

#Passing Diferent DAta Types:

def my_list(fruits):
    for x in fruits:
        print(x)

my_fruits=["apple","Mango","Guava"]
my_list(my_fruits)     

##Return Values:

def my_function():
    return ["apple","banana","Carrot"]

fruits=my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

#Arguments before / are positional-only, and arguments after * are keyword-only:
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)

## 3. Arbitary positional Arguments: *args  ------------------------>

#If you do not know how many arguments will be passed to your function, add a  * before parameter name.
#The function will recieve a tuple of arguments and can access the items accordingly.

def my_function(*kids):
    print("The youngest child is ",kids[2])
    

my_function("Rishi","Varun","tarun") 

def arg_function(*args):
    print("Type ",type(args))              # <tuple>
    print("The First argument ",args[0])
    print("The second argument ",args[1])
    print("All passed arguments ",args)

arg_function("Shree","Karim",5,7,8,"SHEELA") 

# Using *args with Regular arguments:***************************************************************************

def say_hello(greeting,*names):
    for name in names:
        print(greeting,name)
say_hello("Hello","Uncle","Papa","Aunty") 

#A function that calculates sum any number of values:
def my_sum(*num):
    sum=0
    for i in num:
        sum+=i
    return sum
print(my_sum(1,3,5,6,8,9))  
print(my_sum(3,4))
print(my_sum(45,67,89,7,6,5,4,32,1))

#Finding maximum number->
def max_value(*numbers):
    if len(numbers)==0:
        return None
    max=numbers[0]    
    for num in numbers:
        if num > max:
            max=num
    return max

print( "The maximum value is",max_value(9,5,2,89,67,45,78))   

#4.Arbitary keyword arguments: **kwargs ---->

# When you do not know how many keyword arguments will be passed to your function.
#The function will recieve a  dictionary of arguments.

def my_func(**kid):
    print("His last name is ",kid["lname"])

my_func(fname="Akash",lname="Sharma",age="23")

## Unpacking List:

def my_function(a,b,c,):
    return a+b+c
numbers=[1,2,3,4,5,6]
my_function(*numbers)  # Same as my_function(1,2,3,4,5,6)

# Unpacking dictionary:

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")





