#<--------------------------------Python decorators--------------------------------------->

# Real Analogy: If i want to decorate myself (I am a one function) then i will go to a professional-decorator(Another function) and 
#will return as new decorated-person(decorated-function)

# So, decorator is a function that takes another function as input and returns a new function.
#PROCESS: 1.Define the decorator first
#         2.Apply it with @decorator_name above the function

#Before diving into Decorators,We must have to understand the functions deeply and its features.

#--------------->Functions are Objects----->:
#**FUNCTIONS ARE JUST EXECUTABLE OBJECTS.
# Defining a function does not run it.
# () ----> is a button to Turn-On
# ()------> without this ,python treats it as data

x=10        # integer object stored somewhere in memory
print(x)
print(type(x))
print(id(x))                              # Memory Location
#------------------

def greet():
    print("Hello")

    #if functions are also object:

print(greet)        # So, without ()--> greet is just a data ( an object).Here python just prints what greet is pointing to in memory
print(type(greet))  #With  ()--> Python executes the function
   #So,greet is not the code
   # "greet" is a refrence to a function objects in memory 


   ##What is actually happens:
        # def greet():     |
        #   print("Hello") |
        #                  |-------> When python reads this:1.It creats a function object in memory.
        #                                                   2.It stores the code inside it.
        #                                                   3.It assigns the name "greet" to point to that object.
        #   1.greet() ---->Execute function
        #   2.Inside Function-->prints "Hello"
        #   3.Functions returns None:no return statement                                                          #Question1. Integer prints their value, functions print their identity.But both are objects.Why?
        #   4.print(None)                                                         # Answer:Integers and functions are both objects, but their “data” is different in nature.
                                                                             #Python chooses how to display an object based on its type.
                                                                             # So,Object decides how they wanted to be displayed.


# greet ---Function object(data)                                        #######print("Return vs print:")
# greet() --- Execute Function                                                   #1 print()-->Just dhows output
# print(greet) --- Show object info                                                 #greet()
 # **pint(greet()) -- SHOW RETURNED VALUE                                           #print(greet())   # prints Hello but return None

                                                                                #2. return--->
                                                                                    #   '''       1.Sends a value back to the caller
                                                                                    #             2.Stops function execution immediately
                                                                                    #             3.Value can be stored, passed, or reused '''


# NAME---->OBJECT----->CODE

#Why this matters(REAL USES)? 
     #BEACUSE ONCE A FUNCTION IS JUST A data, YOU CAN:
       #1. Assign it:
#                 x=greet
#                 x()
       #2. Pass it: Function as parameter or passing function as arguments
#               def execute(func):
#                        func()               # func----->greet function object
#               execute(greet)                 #WRONG: execute(greet())--->
 
                   #NOTE: 1. We passed greet without ()
                   #      2.That means we passed the function object       
                   #      3. func now points to greet                     Inside execute:func()------>Actually calls greet()
                   # execute(greet())------------>This passes the result ,not the function

                   #Passing a function means passing the function object,not executing.
                #Execution happens when only () is used.

        #3.Return it :
        # 
        #         



#_________________________Name Vs Object_______________________________________________________

# Name is just a label which does not contain data or value.
# It points to an object.
# x= 10  ; x-->name , 10--->Object
# Object: A piece of data in memory which has 1.Type 2.Value 3.Identity(memory location)
#######Assignment(=) does not copy data  #######
  # a=10 
  # b=a     That does not means that data 10 is copied to b
  # a---->10  b--->10 That means one object (10) with two name a and b
######### Changing a name does NOT mean change the object
  # x=12
  # x=13
  # What happens is :  now,x---->13  12---->no name which pointing to it
  # The object 12 still exists (for now),but x no longer points to it
  ## SAME RULE for ALL Objects(Including Functions)
  #  def greet():
  #       print("Hello")
  # Memory : greet----->function object   greet is just a name
  # So, we can also do: x=greet
  # So, x()---It means x points to greet and greet points to function object and ()--->executes that function object
  # Therefore, greet---->function object <-------x
  #  suppose; x=greet
  #  but now; x=10
  # Now: x--->10 but still greet--->function object
  # OBJECT DOES NOT KNOW THEIR NAME.
  # The objcet 10 does not wheather it is called a or b
  # Name lives in scopes, namespaces
  # #However, object lives in Memory 
  #* Names are not variables in python.In python terms: A "Variable" is just a name bound to an object
  # Variable just a refrence not a storage.
#____________________________________________________________________________________________________________________________

 #***********Function Inside function***************    
 #def creates a function object.It does not run the function.Running only happens with()
print("_________________")

#STEP1: What does function inside function  means is "You define a function while another function is running."

# def outer():                                              # outer-->function object is created
#     def inner():
#         print("Hello from inner.")
                                   #Here,When python sees thiss;*It sees def outer
                                   #                            *Creates only the outer function object
                                   #                            *It doess NOT create inner yet
                                   #    outer----> A Function Object.  inner does NOT exist yet.

    #Here in step 1 only outer-->function object is created.No existance of inner-->object                               
# STEP2.When outer() is called:
                                         
def outer():
    def inner():
        print("Hello from inner")

outer()                           #Here, *1.Python jumps insidee outer
                                  #      *2. it reaches :- def inner()                      
                                  #                           print("Hello from inner")
                                  #                       -Python creates new function object
                                  #                       - Binds name "inner" to it.   inner---->a new function object
                                  #                       -inner exists only inside outer
    # Python here in step 2 after calling outer() only Creates a new function object---names it--->inner
    # Stores its code
    # Keeps it inside Outer
    # Nothing is displayed on display of outer() Because inner was created but not executed

# STEP3. 

def outer():
    def inner():
        print("Hello from inner")
    inner()                        # Now python sees (),
outer()                            #Executes the function object inner points to
                                   #Here,Python jumps inside inner ======>print("Hello from inner") 
                                   # inner finishes and control is back returned to outer  

    #When inner() finishes, nothing is transferred to outer() because inner() only prints and return None, and outer() does not capture it.
# So,on display only Hello from inner will be displayed
def outer():
    def inner():
        print("Hello from inner")
        return 100
    x = inner()
    print("Value received in outer:",x)
outer()                                       # Value Recieved in outer:100
y=outer()  
print(y)                                      # None:becuase outer is returning None

#STEP4.

# As in python functions are objects:
#                          So, once outer() ends--:Local names are destroyed and inner disaapers
#WHEN outer()  runs ,Python creates  inner , then executes it, and then destroys it when outer() ends.

def outer():
    def inner():
        print("Hello from inner")
    return inner  ## MOST IMPORTANT: Here, This does not mena "Run inner" .It means "Give the function object inner back to whoever called outer()"
x=outer()   # x -----> inner function object
print(x)    # NOw x is just a data

#NOTE:::::What happens to inner now?--->* inner does not disappear
#                                       * Because x still refrences it.
#          THIS IS THE KEY DIFFERENCE FROM BEFORE

x()           # Calling the returned function