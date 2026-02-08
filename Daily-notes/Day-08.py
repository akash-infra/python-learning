# #************************************if-elif-else***************************************************************************

age=20
if age>=18:
    print("YOu are eligible.")
    print("You can vote.")
    print("You are adult now")

is_logged_in=True
if is_logged_in:
    print("Welcome back!")

a=33
b=33
if a>b :
    print("a is greater than b")
elif a<b :
    print("a is less than b")
elif a==b :
    print("a is eqqual to be")

# Python evaluates the conditions from top to bottom. As soon as it finds a condition that is True , it executes that block and 
# skips all remaining conditions.
# Only the first True condition will be executed even if multiple conditions are true,Python stops after executing the first matcching block

age = int(input("Enter your age:"))
if 0 < age < 13:
    print("You are a child.")
elif 13 < age < 20 :
    print("You are a teenager.") 
elif 20 < age < 60 :
    print ("You are a adult.")
elif age >= 60 :
    print("You are a senior.")  
else:
    print("invalid age.")    

# else provides  adefault action when none of the previous condition are true. It means catch-all   for any scenerio not covered by
# you if and elif statements.
temprature=float(input("Enter the wheather here: ")) 
if temprature > 30:
    print("Its hot outside.")
elif temprature > 20 :
    print("Its warm outside.")
elif temprature > 10 :
    print("Its cool outside.")
else :
    print("It's cold Outside.")    

username="akash" #username=input("eneter your username: ")
if len(username)>0:
    print(f"Hii {username}")
else:
    print("Error:Username can not be empty.")    

# SHORTHAND if statements:
a=5
b=2
if a>b: print("a is greater than b")   
print("a ise big") if a>b else print("b is bigger.")

#Assigning  avalue with if-else:
a=10
b=89
bigger=a if a>b else b
print("Bigger is: ",bigger)

# Using Logical operators:
username=input("Enter Username: ")
password=input("Enter Password here: ")
is_Verified=True
if username and password and is_Verified:
   print("Login Successu")
else:
    print("login failed") 

# Nested if    :

age=25
has_license=True
if age>=18:
    if has_license:
        print("Go!You can drive.")
    else:
        print("Pay Chalan")
else:
    print("Too young to drive")  

uname="Akash" 
pswd="Akash234"
is_active=True
if uname:
    if pswd:
        if is_active:
            print("Login Successul.") 
        else:
            print("Account is inactive.") 
    else:
        print("Password is required.")
else:
    print("Please Enter Username.")  


# pass    statements  ;
# if statement can not be empty, but in some case there isa i-statment with no content ,put in the pass to avoid error
z=10
v=29   
if z>v:
    pass
#The pass statement is a null operation-nothing happens when it executes.It servesa as a placeholder.
# Why pass?
# 1.When you're creating code structure but haven't implemented the logic yet
# 2.When a statement is required syntactically but no action is needed
# 3.As a placeholder for future code during development
# 4.In empty functions or classes that you plan to implement later 

value=27
if value >0:
    print("Positive Velue")
elif value==0:
    pass
else:
    print("Negative Value.")  


#***************************************************Practice***************************************************************


# #1.WAP to display the last digit of a number. (Don’t use indexing for this) 
num= int(input("Enter the number: "))
if num < 10:
    print(num)
else:
    last=num%10
    print("Last digit of entered number is: ",last)    

#2.WAP to check if a single character is a vowel or not.
character=input('Enter a single character: ')
if character.lower() in "aeiou":
    print("It's a vowel")
else:
    print("It's a not a vowel") 

# #3. WAP to check if a number is even or odd where the number is taken as input
num=int(input("Enter a number: "))
if num%2==0:
    print("Number is even.")
elif num==0:
    print("Error.")    
else:
    print("Number is odd")    

#4.WAP to check if the 3rd last character of a string is a vowel or not.

str=input("Enter the content here: ")
print(str[-3])
if str[-3].lower() in "aeiou":
    print("It's a vowel.")
else:
    print("Its not a Vowel.") 

#5. Check if the first and last number of a list is same or not. Take a pre-defined list in the code itself.
lst= list(input("Add Number List :"))
if len(lst)==0 or len(lst)==1:
    print("Can not compare")

elif lst[0]==lst[-1]:
    print("Equal Numbers at end points.")
else:
    print("List is not same at end points") 

#6. WAP to calculate percentage of a student through 5 subjects. Take marks as input from the user.
#Using percentage print which grade the student has scored. 

m=int(input("Marks in Math: "))        
h=int(input("Marks in History: "))        
s=int(input("Marks in Science: "))        
e=int(input("Marks in English: "))        
a=int(input("Marks in Arts: "))
total=m+h+s+e+a
perc= float(100*total/500)
print("Percentage o student is: ",perc)
if perc > 90:
    print("A+ grade")
elif 90>=perc>80:
    print("A Grade")
elif 80>=perc>70:
    print("B+ Grade")
elif 70>=perc>60:
    print("B Grade")
elif perc>33 and perc<=60:
    print("You are pass.")
else:
    print("You are fail.")  

#7. WAP to print the day based on the number input.

d={1:"Monday", 2:"Tueseday", 3:"Wednessday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
num=int(input("Enter the number: "))
if num in range(1,8):
    print(d[num])
else:
    print("Invalid Day.") 

############################## Match Statements:

# Syntax:      match <expresssion>:
#                   case x:
#                        code block
#                   case y:
#                        code block
#                   case z:
#                        code block


#1.The match expression is evaluated once.
#2.The value of expression is compared with the values of each case.
#3.If there is a match ,the associated block of code is executed.

day=int(input("Enter the Day No. :"))
match day:                            #The value of evaluated expression will be compared to each case.
    case 1:
        print("Monday")
    case 2:
        print("Tueseday")
    case 3:
        print("Wednessday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7: 
        print("Sunday") 
    case _:                        #When there is a no match ,this will be executed.
        print("This day does not exist") # This is default which always will match.
 #Use the | pipe character to as an operator in case evaluationto check for more than one value match in one case.

day = 5
match day:
    case 1 | 2 | 3 | 4 | 5 :
        print("Today is weekday.")
    case 5 | 6:
        print("It's Weekend,let's go for movie") 

# We can add if statements in the case evaluation  as an extra condition:

month = 5
day = 3
match day:
    case 1|2|3|4|5 if month == 4:
        print("A weekday in April.")
    case 6|7 if month == 5 :
        print("A weekend in May.")
    case _:
        print("No match.")                                




    
      
    
