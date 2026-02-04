#This is Day-04.py
#In this we will learn about basic operations and operatores in Python.
########################## Arithmetic Operators###############################
# The arrithmetic operators are as follows:
#1. Addition (+)
print ("Addition of two numbers is:", 5 + 3)
#2. Subtraction (-)
print("Subtraction of two numbers is:", 5 - 3)
#3. Multiplication (*)
print ("Multiplication of two number is", 5 * 3)
#4. Division (/)
print ("Division of two Numbers is :",5 / 3)
#5. Floor Division (//)
print ("Floor Division of two numbers is", 5 // 3)
#6. Modulus (%)
print ("Modulus of two number is :" , 5 % 3)
#7. Exponentiation (**)
print ("Exponential of two number is:" , 5**3)
#*******************************Practice Exercise*******************************
#1.Checking precedence of Arithmetic Operators
print("The Result of 9+24/8-1*23//2**2 is:", 9+24/8-1*23//2**2)
#2. Write a program to calculate the area of a rectangle.
l=23 ; w=12
area = l*w
print ("The area  of rectangle is : ",area) 
#3. Write a program to calculate the perimeter of a rectangle.
l=43 
w=76 
perimeter = 2*(l+w)
print("The perimeter of Rectangle is :", perimeter)
#4. Write a program to calculate the area of a circle.
radious=7 ; pi=3.14
area_circle= pi*radious**2
print("Area of the circle is:", area_circle)
#5. Write a program to calculate the circumference of a circle.

r=12 ; pi=3.14
circum=2*pi*r
print("Circumference of circle is:", circum)
#6. Write a program to calculate the simple interest.
principle=1500 ; rate=4.3 ; time=6
simple_intrest=(principle*rate*time)/100
print("Simple Intrest is:", simple_intrest)
#7. Write a program to calculate the compound interest.
p=2000 ; r=5 ; t=23
compound_intrest=p*(1+r/100)**t
print("Compound Intrest is:", compound_intrest) 

############################## Comparison Operators ##############################
# The Comparison Operators are as follows:
# 1. Equal to (==)
#       Equals to operator checks whether the two values are equal or not.
#       it does not assign value rather it compares the values.
#       For assigning value we use single equal to operator (=)
#       In memory it returns True or False.
#       It displays True if both values are equal otherwise it displays False.
a=9 ; b=8
print("Is a equal to b?:",a==b)
#2. Not Equal to (!=)
      #Not equal to operator checks whether the two values are not equal.
      #It returns True if both values are not equal otherwise it returns False.
print(a!=b)
#3. Greater than (>)
      #Greater than operator checks whether the left value is greater than right value.
      #It returns True if left value is greater otherwise it returns False.
print(a>b)
#4. Less than (<)
      #Less than operator checks whether the left value is less than right value.
      #It returns True if left value is less otherwise it returns False.
print(a<b)
#5. Greater than or Equal to (>=)
      #Greater than or equal to operator checks whether the left value is greater than or equal to right value.
      #It returns True if left value is greater than or equal otherwise it returns False.
print(a>=b)
#6. Less than or Equal to (<=)
      #Less than or equal to operator checks whether the left value is less than or equal to right value.
      #It returns True if left value is less than or equal otherwise it returns False.
print(a<=b)
# #*******************************Practice Exercise*******************************
# #1. Write a program to compare two numbers and print the largest one.
a=46 ; b=98
if (a>b): 
    {
        print("The largest number is:",a)
    }
else:
  {
    print("The largest Number is:",b)
}
#2. Write a program to check whether a number is even or odd.
num=29
if(num%2==0):
   {
      print("The number is even")
   }
else:
   {
      print("The number is odd")
   }
#3. Write a program to check whether a number is positive or negative.
number=-6

if(number>0):
   {print("The number is +ve")}
else:
   {print("The number is -ve")}

#4. Write a program to check whether a year is leap year or not.
year=2029
if(year%4==0):
   {print("The year is Leap Year")}
else:
   {print("The year is not a Leap Year")}


#*************************************************************
#List of all operators in python category wise               *
#1. Arithmetic Operators: +, -, *, /, %, //, **              *
#2. Comparison Operators: ==, !=, >, <, >=, <=               *
#3. Logical Operators: and, or, not                          *
#4. Assignment Operators: =, +=, -=, *=, /=, %=, //=, **=    *
#5. Bitwise Operators: &, |, ^, ~, <<, >>                    *
#6. Membership Operators: in, not in                         *
#7. Identity Operators: is, is not                           *
#  ***********************************************************    
                                               
######################3lLogical Operators##############################
# The Logical Operators are as follows:
#1. and Operator
      #The and operator returns True if both the statements are true otherwise it returns False.
x = 5
print(x > 3 and x < 10)  # Returns True because both conditions are true
#2. or Operator
        #The or operator returns True if one of the statements is true otherwise it returns False.
x = 5
print(x > 3 or x < 4)  # Returns True because one condition is
#3. not Operator
        #The not operator reverses the result, returns False if the result is true.
x = 5
print(not(x > 3 and x < 10))  # Returns False because the result is true
#*******************************Practice Exercise*******************************

#1. Write a program to check whether a person is eligible to vote or not.
age=18 ; voterID=True
if(age>18 and voterID==True):
   {print("The Person can Vote")}
else:
   {print("The person cannot vote.")}

#2. Write a program to check whether a person is eligible for a senior citizen discount.
age=65 ; buyproducts=54
if (age>65 or buyproducts>54):
   {print("The person is eleigible for senior citizen discount")}
else:
   {print("Not eligible for senior citizen discount")}

#3. Write a program to check whether a number is not in a given range.
num=45
if (num>10 and num<40):
   {print("The numebr is in the range")}
else:
   {print("The number is not in the range")}
#4. Write a program to check whether a string is not empty.
str="Hello"
if (not(len(str)==0)):
   {print("The string is not empty")}
else:
   {print("The string is empty")}

   ############################### Assignment Operators ##############################
# The Assignment Operators are as follows:
#1. Equal to (=)
        #The equal to operator assigns the value on the right to the variable on the left.
a = 5
print("The value of a is:", a)      
#2. Add AND (+=)
        #The add AND operator adds the right operand to the left operand and assigns the result to the left operand.
a=9 
a+=4 #This is equivalent to a = a + 4
print("The value of a is:",a) # The value of a is: 13
#3. Subtract AND (-=)
        #The subtract AND operator subtracts the right operand from the left operand and assigns the result to the left operand.
b=8
b-=b #This is equivalent to b = b - b
print(b) # The value of b is: 0
#4. Multiply AND (*=)
        #The multiply AND operator multiplies the left operand by the right operand and assigns the result to the left operand.

c=56
c*=2 #This is equivalent to c = c * 2
print(c) # The value of c is: 112
#5. Divide AND (/=)
#     #The divide AND operator divides the left operand by the right operand and assigns the result to the left operand.
d=43
d/=2 #This is equivalent to d = d / 2
print(d) # The value of d is: 21.5
#6. Modulus AND (%=)
        #The modulus AND operator takes modulus using two operands and assigns the result to the left operand.      
r=65
r%=7 #This is equivalent to r = r % 7
print(r) # The value of r is: 2 
#7. Floor Divide AND (//=)
        #The floor divide AND operator performs floor division on operands and assigns the result to the left operand.
        #       Floor division is a division in which the digits after the decimal point are removed.      
m=54
m//=5 #This is equivalent to m = m // 5 
print(m) # The value of m is: 10
#8. Exponent AND (**=)
        #The exponent AND operator performs exponential (power) calculation on operators and assigns the result to the left operand.
n=3
n**=4 #This is equivalent to n = n ** 4
print(n) # The value of n is: 81
#9. 
x=27
x|=9
print("The value of x is: ",x)

#10. WALRUS OPERATOR:
#Walrus operator lets you assign and use a  value in same expressison
# x=80
# if x > 10:
#    print(x)
# if (x=10)>5:   # error
#    print(x)
if (x:=10)>2:
   print(True)

#*******************************Practice Exercise*******************************
#1. Write a program to swap two numbers using assignment operators.
a=5 ; b=10
temp=a ; a=b ; b=temp
print("after swapping a is:",a)
print("after swapping b is:",b)
#2. Write a program to calculate the total cost of items purchased using assignment operators.
i1=270 ; i2=430 ; i3=150
t=0
t+=i1
t+=i2
t+=i3
print("The total cost of items purchased is:",t)
#3. Write a program to calculate the remaining balance after making a purchase using assignment operators.
balance=5000
purchase=1550
balance-=purchase
print("The remaining balance after purchase is:",balance)
#4. Write a program to calculate the final score of a player after adding bonus points using assignment operators.
score=1200  
bonus=300
score+=bonus    
print("The final score of the player is:",score)
#5. Write a program to calculate the area of a square using assignment operators.
side=8
area=0
area=+side**2
print("The area of square is:",area)
#6. Write a program to calculate the total distance traveled using assignment operators.
distance=0
distance+=50
distance+=30
print("The total distance traveled is:",distance)

############################### Bitwise Operators ##############################
# The Bitwise Operators are as follows:
#1. AND (&)
      #The AND operator compares each bit of the first operand to the corresponding bit of the second operand.
      #If both bits are 1, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0.
a=4 # (in binary: 0100)
b=5 # (in binary: 0101)
print ("the result of bitwise AND (&) is:", a & b) # Here, 0100 & 0101 = 0100 (which is 4 in decimal)
#2. OR (|)
      #The OR operator compares each bit of the first operand to the corresponding bit of the second operand.
      #If either bit is 1, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0.
a=4 # (in binary: 0100)
b=5 # (in binary: 0101)
print ("the result of bitwise OR (|) is:", a | b) # Here, 0100 | 0101 = 0101 (which is 5 in decimal)
#3. XOR (^)
      #The XOR operator compares each bit of the first operand to the corresponding bit of the second operand.
      #If the bits are different, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0.
a=4 # (in binary: 0100)
b=5 # (in binary: 0101)
print ("the result of bitwise XOR (^) is:", a ^ b) # Here, 0100 ^ 0101 = 0001 (which is 1 in decimal)
#4. NOT (~)
      #The NOT operator is a unary operator that inverts all the bits of its operand.
a=4 # (in binary: 0100)
print ("the result of bitwise NOT (~) is:", ~a) # Here, ~0100 = 1011 (which is -5 in decimal in two's complement representation)
#5. Left Shift (<<)
      #The left shift operator shifts the bits of the first operand to the left by the number of positions specified by the second operand.
a=4 # (in binary: 0100)  
b=2 # number of positions to shift
print ("the result of left shift (<<) is:", a << b) # Here, 0100 << 2 = 0001 0000 (which is 16 in decimal)
#6. Right Shift (>>)
      #The right shift operator shifts the bits of the first operand to the right by the number of positions specified by the second operand.
a=4 # (in binary: 0100)
b=2 # number of positions to shift
print ("the result of right shift (>>) is:", a >> b) # Here, 0100 >> 2 = 0000 0001 (which is 1 in decimal)
#*******************************Practice Exercise*******************************
#1. Write a program to perform bitwise AND operation on two numbers.
a=24 ; b=65 ; c=90
result=a&b
result&=c #This is equivalent to result = result & c
print ("The result of bitwise AND among three numbers is:", result)
#2. Write a program to perform bitwise OR operation on two numbers.
a=34 ; b=78 ; c=56
result=a|b
result|=c #This is equivalent to result = result | c
print ("The result of bitwise OR among three numbers is:", result)
#3. Write a program to perform bitwise XOR operation on two numbers.
a=45 ; b=23 ; c=67  
result=a^b
result^=c #This is equivalent to result = result ^ c
print ("The result of bitwise XOR among three numbers is:", result)
#4. Write a program to perform bitwise NOT operation on a number.
a=34
result=~a
print ("The result of bitwise NOT operation is:", result) # it is also termed as one's complement

########################################### Membership Operators ##############################
# The Membership Operators are as follows:

#1. in Operator
        #The in operator checks whether a value is present in a sequence (like a list, tuple, or string).
        #It returns True if the value is found in the sequence, otherwise it returns False.

numbers = [1,2,3,4,5,8]
print(3 in numbers) # Returns True because 3 is present in the list
print(7 in numbers) # Returns False because 7 is not present in the list
#2. not in Operator
        #The not in operator checks whether a value is not present in a sequence (like a list, tuple, or string).
        #It returns True if the value is not found in the sequence, otherwise it returns False.
numbers = [1,2,3,4,5,8]
print(3 not in numbers) # Returns False because 3 is present in the list
print(7 not in numbers) # Returns True because 7 is not present in the list
#*******************************Practice Exercise*******************************
#1. Write a program to check whether a character is present in a given string.
str="Hello,My name is Akash"
char='A'  ; a=3
if (char in str):
    {print("The character is present in the string")}
else:
    {print("The character is not present in the string")}
#2. Write a program to check whether an element is present in a given list.
lst=[12,34,66,87,90]
element=98
if(element in lst):
    {print("The element is present in the list")}
else:
    {print("The element is not present in the list")}   

# How actually in works: membership operator check wheather  a value exists in container using equality(==),not memory identity
x=[1,2,3]
y=[1,2,3]
print( y in x) # False
#Because python compares each element of  x with y
# Elements x are 1,2,3
#    y[1,2,3] ==1 X, ==2  X, ==3 X
# y is a list , not an element of x
# However, y in [x] --->True
# Here , [a] is a list with one element .That element is  a itself.[a]--->[[1,2,3]]
#b==a : [1,2,3]==[1,2,3]
#

    ################################## Identity Operators ##############################
# The Identity Operators are as follows:
#1. is Operator
        #The is operator checks whether two variables point to the same object in memory.
        #It returns True if both variables point to the same object, otherwise it returns False.    
a = [1, 2, 3]
b = a
print(a is b)  # Returns True because both a and b point to the same object
c = [1, 2, 3]
print(a is c)  # Returns False because a and c point to different objects
#2. is not Operator
   #The is not operator checks whether two variables do not point to the same object in memory.
   #It returns True if both variables do not point to the same object, otherwise it returns False.
a = [1, 2, 3]  
b = a
print(a is not b)  # Returns False because both a and b point to the same

c = [1, 2, 3]
print(a is not c)  # Returns True because a and c point to different objects     
# ende of Day-04.py

# Tomorrow's topic is Day-05.py : Python Data Types and Type Conversion








