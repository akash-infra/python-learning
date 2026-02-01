#**************************************Introduction*********************************************************

"""
...................    Theoritical Concepts like what is python,history of python,features of python,installation of python,IDE's etc  .................

"""
#**************************************Comments********************************************************************

# This is a comment.

#In this  we will learn about Comments,Escape sequences.


# To comment multiple lines-->Slect them and Use Ctrl +/

# This way you can comment multiple lines at once.
print("This is Day-02 to learning python") #This is a print statement.
# '''
# Hii My name is akash.
# '''
print("Hello, I am Day-01.py\nThis is the new line after escape sequence.")
#Double quotes inside double quotes using escape sequence
print ("He said,\"I am learning Python.\"")
#Single quotes inside single quotes using escape sequence
print("It\''s a beutiful day.'\nIsn't it?")
print("This is a backslash: \\")
print("First Line\nSecond Line\nThird Line")
#Seperator and End parameters in print function
print("Heelo", "World"  , "Dakin","Last", sep="~", end="***\n")#Custom seperator and end
print("This is the next print statement after custom end.")

#******************************************Indentation in Python*************************************************************

#Indentation refres to the spaces at the begining of a code line.
#Python uses indentation to indicate a block of code.
if 5 > 4:
 print(1+1)    
 print(5+4)
#The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.
# You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:
a=10 ; b=5
if a > b:
   print(a)
   print(a-b)
 #          print("a is greater than b")  #This will cause an error because the indentation is not consistent.
 
print("This is outside the if block.")   


#**********************************************Python print Statements***************************************************************




# In python a statements usuallu ends with the line ends.You do not need ; (semicolon) like in many other programming language.
# These statements are executed one by one  as they are written

print("Hii, ia m a first line statement")
print("I am second line statements") 
print("i am third line statements") 
#However, if you want to write multiple statements in a single line, you can use semicolon ; to separate them.
x=5 ; y=4
print(x) ; print(y) ; print("This is multiple statemenets in one line writen") #    Each print-function-call prints text on a new line.
#But using multiple statements in a single line is not a good practice. It is better to write each statement in a new line for better readability.
#if you want to print multiple words in a single line you can use end parameter of print function.
print("Hello world!", end=" ") ; print("Welcome to Python programming.")
print("Akash", end=" ")
print("is learning Python.")


