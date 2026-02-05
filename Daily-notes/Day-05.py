#*****************************************STRINGS*********************************************************************************



#Strings must be enclosed in ( " ") or ( ' ') or ( '''  ''' ) or ( """  """ )
#Strings are immutable,which means once a string is created, it cannot be changed.
#Multiple lines strings can be created using triple quotes.
#Strings can be accessed using indexing and slicing.

print("hello world") 
print('Hii Akash!')
print('"Sachin Tendulkar" was a great cricket player.')
a='''This way we learn try,fail and repeat.This is the complete way of learning
       .However this way representing the multiline strings'''
print(a)

# 1.Strings are arrays of characters.Individual character can be accessed using indexing(First character having index 0).
str1="Hello, welcome to python programming."
print(str1[9]) #This will print the character at index 9 which is 'e'
print(str1[0])
#2. Looping through  strings:
for x in "banana":
    print(x)

#3. String Length:  Use len() function to get the length of string.

#The len() function returns the number of characters in a string, including spaces and special characters.
str2="Aka     sh      sharm  a"
print(len(str2))

#4. Check String: Use the 'in' keyword to check if a substring exists in a string.

str3="Akash is brother of Maneesh.Maneesh brother of Akash."
print("brother" in str3) #This will return True because 'brother' is present in str3
print("sister" in str3) #This will return False because 'sister' is not present in str3
if "Maneesh" in str3:
    print("Yes, 'Maneesh' is presnet in the text.")
if "Suresh" not in str3: #This will return True because 'Suresh' is not present in str3
    print("NO, 'Suresh' is not present in the tex") 

###### 5. String Slicing: You can extract a portion of a string by using slicing.#####################################

# Slicing is done by specifying the start and end index of the substring you want to extract.
# The syntax for slicing is: string[start:end]
# The start index is inclusive, while the end index is exclusive.
b="KritikaSrivastava." 
print(b[2:8]) 
print(b[:7]) #This will print from index 0 to index 6.This is called slicing from the beginning.
print(b[5:]) #This will print from index 5 to the end of the string.This is called slicing to the end.
   #Negative Indexing: Negative indexing means starting from the end of the string.
   #The last character has index -1, the second last character has index -2, and so on.
   #The start index should be less than the end index when using negative indexing.
c="LearningPythonIsFun"
print(c[-4:-1]) #This will print from the 4th last character to the 2nd last character.
                #-1=n will not be included.
print(c[-1:-4])#This will print an \empty string\ because the start index is greater than the end index.

  ##. VERY IMPORTANT RULE ABOUT SLICING:
   #.       STEP             DIRECTION         CONDITION
   #  Positive(+1)default         Left to Right        Start index < End index  
   #  Negative(-1)                 Right to Left        Start index > End index
   # Yaani humm jidhar move kar re hein uss direction ka end index bada rahega hamesha.
   #print(str[start:end:step]) #step is optional # step indicates the increment between each index.
   #By default step is +1.
d="ABCDEFGHIJKLMNOPQRSTUVWXYZ"   
# print(d[1:10:1]) #This will print from index 1 to index 9 with a step of 1.
# print(d[1:10:2]) #This will print from index 1 to index 9 with a step of 2.
# print(d[10:1:-1])#This will print from index 10 to index 2 with a step of -1.
# print(d[-1:-10:-3])
print(d[-1:0:-1])
print(d[-1::-1]) #This will print the entire string in reverse order.
print(d[::-1]) #This will also print the entire string in reverse order.
# print(d[-6:-1])
# print(d[-6:1:1]) 
print(d[-1:-6]) #This will print an empty string because the start index is greater than the end index and step is positive.
print(d[-1:-6:-1])#This will print from the last character to the 6th last character in reverse order.

print(d[-6:-1:-1]) #This will print an empty string because the start index is less than the end index and step is negative.
print(d[-6:-1]) #This will print from the 6th last character to the 2nd last character.

#6.Modify Strings:
   #Strings are immutable,which means once a string is created, it cannot be changed.
    #However, you can create a new string by modifying an existing string.
    # Python has several built-in methods that can be used to modify strings.
str4="   Hii!  My name is Ramesh.    "
print(str4.upper())  #This will convert all characters to uppercase.
#print(upper(str4)) ##The problem is that there is no built-in function called upper() in python.Difference between method and function is that method is associated with an object while function is not.
print(str4.lower())  
print(str4.strip()) #Removes Whitespaces: This will remove all leading and trailing whitespaces from the string.
print(str4.replace("Ramesh","Akash")) #This will replace all occurrences of "Ramesh" with "Akash".
print(str4.split(" , ")) #This will split the string into a list of substrings based on the delimiter ",".
print(str4.rsplit("~"))
print(str4.capitalize()) #This will capitalize the first character of the string.
print(str4.title()) #This will capitalize the first character of each word in the string.
print(str4.count("a")) #This will count the number of occurrences of "a" in the string.
print(str4.find("name")) #This will return the index of the first occurrence of "name" in the string.
print(str4.index("Ramesh")) #This will return the index of the first occurrence of "Ramesh" in the string.
#If the substring is not found, find() returns -1 while index() raises an error
print(str4.join(["Hello","World","!"])) #This will join the list of strings into a single string with the separator as str4.

#6. String Concatenation:
# You can concatenate strings using the + operator.
#It combines two or more strings into a single string without any spaces in between.
p="Python" ; q="is a" ; r="programming language."
s=p+q+r
print(s) #without spaces
s=p+" "+q+" "+r
print(s) #with spaces

#7. String Formatting:
# String formatting is used to insert variables or values into a string.
name="Akash" ; age=20
# print("My name is:",name, "and i am ",age, "years old.") 
# print("My name is :"+name+"and i am "+age+"years old") #This will cause an error because age is an integer and cannot be concatenated with strings directly.
print("My name is "+name+ "and i am "+str(age)+ "years olde. ") #This will work because we are converting age to string using str() function.

#Another way of string formatting is using f-strings (formatted string literals) available in Python 3.6 and above.
age=98
#txt="My name is john , i am" + age
#print(txt) #This will cause an error because age is an integer and cannot be concatenated with strings directly.
txt= f"My name is john , i am {age} years old."
print(txt)

# A placeholder {} is used to insert the operations , functions and modifiers inside the string.
rate=98
txt= f"This fruit tree is {age+100} years old and the rate of its fruit is {rate*2} per kg."
print(txt)
 #A modifier can also be used inside the placeholder to format the value.
price=49.56789
txt=f"The price of this oil is {price:.2f} per litre." #This will format the price to 2 decimal places.
print(txt)
# Other modifiers are:
# .3f --> 3 decimal places
# .0f --> no decimal places
# , --> comma as thousand separator
amount=1234567.8910
txt=f"The total amount is {amount:,.2f} rupees."
print(txt)
# You can also use the format() method for string formatting.
quantity=5
txt="I have {} apples.".format(quantity)
print(txt)
run=100
txt= "I ran {} km today.".format(run)
print(txt)


#********************************************************End of strings**********************************************************
 #Revision of strings:
#Strings are sequences of characters enclosed in single quotes, double quotes, or triple quotes.
#sttrings are like arrays of characters.
#We can access individual characters in a string using indexing.
# str1 = "Hii,I  am a string"
# str2 = 'I am single quoted string'
# str3 = '''I am a triple quoted string. I can span multiple lines.'''
# print(str1)
# print(str2)
# print(str3)
# #Accessing individual characters using indexing
# print(str1[0])
# print(str1[1])
# print(str1[2]) 
# print(str1[3])
# print("\"Akash\" is my favourate student.")
#Now let's learn opesrations ons strings.
#1.String slicing
#Slicing is used to extract a portion of a string.
#In cloud computing slicing is very useful to extract specific data from large strings.
msg="This is your  final warning to submit the examiation fees."
print(len(msg)) 
#indexing in strings starts from 0 and spaces are also counted as characters.
print(msg[0:3])
print(msg[0:4])
print(msg[0:5])
print(msg[0:6])
#negative slicing
print(msg[1:9])
print(msg[10:-10]) #This will print from index 10 to the 10th last character.
print(msg[-10:-1]) #This will print from the 10th last character to the last character.
print(msg[0:-2]) #This will print from index 0 to the 2nd last character.
print(msg[-1:1]) #This will print an empty string because the start index is greater than the end index.
print(msg[9:1])#This will also print an empty string because the start index is greater than the end index.
#2.string concatenation
str1="Hello,"
str2=" How are you?"
str3=str1+str2
print(str3)
#3.string repetition
str4="Ha"
str5=str4*5
print(str5)
#4.string methods
#There are many built-in methods available for strings in Python.
#Many built in methods are as follows:
#



