#Chalange01: Check if a string is Palindrome(optimized)  

# Palindrome : A palindrome is a word, sentence, number, or sequence that reads the same: Forward , Backward
# madam , level 

str1="madam"  
str2=""
for ch in str1:
    str2=ch+str2 
if str1==str2:
    print("String is Palindrome")
else:
    print("Not Palindrome")
       # Using Function-->
def is_palindrome(s):
    a=0
    b=len(s)-1
    while a<b:
        if s[a].lower()==s[b].lower():
            return True
        a+=1
        b-=1
    return False 
print(is_palindrome("level"))
print(is_palindrome("Akash"))  



#********************* palindrome practice again

# Check wheather a string is palindrome 


## This is simple logic first striked
str="madam"
rev_str=""
for i in range(len(str)-1,-1,-1):
    rev_str=rev_str+str[i]
if str==rev_str:
    print("Palindrome")
else:
    print("Not Palindrome")

## Second ,better method to check palindrome
### Using Two pointers
def is_palindrome(s):
    a=0
    b=len(s)-1
    while a<=b:
        if s[a].lower()!=s[b].lower():    # lower(), so that string character could be comparedd if capital arrives
         return False
        a+=1
        b-=1
    return True
print(is_palindrome("kanak")) 
print(is_palindrome("")) 
print(is_palindrome("K")) 
print(is_palindrome("12")) 


# => It can handle empty string and single-character and cases also



# CHALLENGE02: Count the frequency of each character in a string  
 
def coun_freq(s):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    return freq 

print(coun_freq("AdidDaADDs")) 

#Second Method Could be like this:

def frequency_counter(s):
    dict={}
    for char in s:
        dict[char]=dict.get(char,0)+1
    return dict 

print(frequency_counter("HabibiHalimaKhalo"))  


#CHALANEGE03 : Find the character that appears the most in a string.
def most_freq_char(s):
    dict={}
    for char in s:
        dict[char]=dict.get(char,0)+1
    max_char=None
    max_count=0
    for char,count in dict.items():
     if count>max_count:
        max_char=char
        max_count=count 
    return max_char,max_count  

print(most_freq_char("adjslfasbfhffj"))
    








