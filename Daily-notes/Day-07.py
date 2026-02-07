#***************************************************Boolean Values********************************************************

#A Bollean is a data type that has only only two values : Truth and False
# True and False must start with capital T and F respectively. truth , false ,TRUE , FALSE are invalid.

#Level-01:
 #Boolean usually comes with comparison operators.
 # ==  : Equal to 
 # =   : Assignment operator
 # !=  : Not equal to
 # >   : Greater than
 # <   : Less than
    # >=  : Greater than or equal to
    # <=  : Less than or equal to
#NOTE : = is assignment , == is comparison

print(5 == 5)
print( 5!= 3)
print(10 > 5)
print(3<7)
print(5 >= 5)
print(4 <= 6)
print(10 == 20)
print(10<=20)

#Level-02:
#You can also use the bool() function to evaluate any value and return True or False.
x="Hello" ; y=10 ; z=0
print(bool(x))
print(bool(y))
# Almost any value is evaluated to True  if it has some sort of content.
# Any string is true ,except empty string " ".
# Any number is True , except 0.
#Any list , tuple , set , dictionary is True , except empty ones.
print("abc")
print(["apple","banana","cherry"])
print(0)
print("")
# Values such as (),[],{},0,"", None  ---> are evaluated to False.
print(bool(()))
print(bool([]))
print(bool({}))      
print(bool(None))
print(bool(0))

#Level-03:
# Boolean from functions:
print("Boolean Functions:")
def myfunction():
    return True
print(myfunction())

def is_even(num):
    return num%2==0
print(is_even(4))
print(is_even(5))

# Level-04:
# Boolean with membership opearator:
fruits=["apple","cherry","orange"]
print("apple" in fruits)
print("guava" not in fruits)

# Level-05:
#boolean with identity (is vs ==):
#  == ----> value comparison
#  is ----> memory location comparison
a=10
b=10
print(a==b)  #True
print(a is b) #True (small inetger catching)
x=[1,2,3]
y=[1,2,3]
print(x==y)  #True
print(x is y) # False ,
 # In python everything is object.
 # “Everything in Python is an object, 
 # but objects may or may not have unique memory locations because Python can reuse immutable objects for optimization.”
 # When do objects share memory :
        #  Small Integers(-5 to  256) , None,True , False ,Empty Value , some string Literals
 # When do objects not share memory :
        # Mutable Objects(almost always) , Large integers , run-time created strings

# PYTHON OBJECTS:
     
          # Object = identity+type+value
          #1.Identity: --->Where the object lives in memory , it never changes during the object's lifetime
             #             x=10 ; print(id(x))
             #            a=[1,2] ; b=[1,2]
             #            print(a is b)   --> False
          #2. type: -------> what kind of object are you,what kind of opeartions are allowed,How the object beahves
             #          print(type("hell0"))  ; print(type(10))  
             # Prefr isinstanceof(x,int)
          #3. value : ------> What do you hold,the actual data inside the object,may change if object are only mutable
#Immutable objects: Value change hui to new object bn jaayegi yaani same object nhi rahegi
# int,floar,bool,str,tuple
x=10
print(id(x))
x=x+1
print(id(x))  
# Both x are two different objects .Here x is a integer which is immutable thats why
# Mutable Objects : Value chnage---->SAME Object
# list,dict,set
list=[1,2]
print(id(list))
list.append(3)
print(id(list))  # Gives the same memory 


    

 


