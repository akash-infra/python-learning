# In this exercise we will practice Strings Rigoriously 
# Question1: Reverse a string WITHOUT using slicing [::-1]
# Do NOT use slicing , Do NOT use reversed() , Do NOT use built-in reverse tricks

str="Cloud"
reversed=""
for i in range(len(str)-1,-1,-1):    #range(Start,Stop,Step)-->[4,3,2,1,0]
    reversed=reversed+str[i]

print(reversed)

# Another method,
#We know strings are iterable
text="Cloud"
reverse=""
for char in text:
    reverse=char+reverse
print(reverse)

# How python treats negative index accessing
text = "DevOps"

for i in range(len(text)):
    print(text[-i], end="") 

print("\n")                                # IMPORTANT!             text[-0]==text[0]
# RESULT:: DspOve 

#Question 2:  Given : log = "SUCCESS 2026-02-12 Server-2 Backup Completed"
            # Extract status , date , server ,message

log = "SUCCESS 2026-02-12 Server-2 Backup Completed"
parts=log.split()
print(parts)
# parts=['SUCCESS', '2026-02-12', 'Server-2', 'Backup', 'Completed']
status=parts[0]
date=parts[1]
server=parts[2]
message=" ".join(parts[3:])
print("Status:",status)
print("Date:",date)
print("Server:",server)
print("message:",message)

##Upgraded Version of above script:
if len(parts)>=4:
    status=parts[0]
    date=parts[1]
    server=parts[2]
    message=" ".join(parts[3:])
else:
    print("log Format is invalid")
    exit()

print(f"Status:{status}")
print(f"Date:{date}")
print(f"Server:{server}")
print(f"Message0:{message}")

#************************************** Again practice of reversing a string

# as a beginer i would go with this 
str="akash"
reverse=str[-1:-6:-1]
print(reverse)

#optimizing this:
def rev_str(s):
    a=len(s)+1
    reverse=s[-1:-a:-1]
    return reverse 
print(rev_str("churan")) 

# Reverse string without slicing

def reverse_string(s):
    reverse=""
    for ch in s:          # We know strings aree iterable
        reverse=ch+reverse
    return reverse 

    
print(reverse_string("KadakPan"))   

## We also know the len,range function in string:
def r_str(s1):
 reve_str=""
 for i in range(len(s1)-1,-1,-1):
    reve_str =  reve_str +  s1[i]           # String behaves like array
 return reve_str
print(r_str("KalaJamuna")) 

# All these give O(n2)  complexity:

# For better solution

def str_reverse(s):
    result=[]
    for i in range(len(s)-1,-1,-1):
        result.append(s[i])
    return "".join(result)
print(str_reverse("ComplexityReduced"))





