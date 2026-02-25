# Given a string, count the number of vowels and consonants. Ignore case. Ignore non-alphabet characters.
# Input: "Hello World!"
# Output: Vowels = 3, Consonants = 7


## My approach 
s="Hello World"
p=0
q=0
for ch in s.lower():
   # if ch.isalpha():
       if ch in "aeiou":
          p+=1
       else:
          q+=1
print("Vowels=",p,end=" ")
print("Consonants=",q)

## Refining it:
### What  if string contains special character , space , number etc. --> That will be counted as consonant obvously

##  -----> isalpha()  : This checks wheather ch is alphabet letter or not.

def count_vow_conso(s):
    a=0; b=0
    for ch in s.lower():
        if ch.isalpha():
            if ch in "aeiou":
                a+=1
            else:
                b+=1
    return a,b

vowels, consonants = count_vow_conso("RamHare1@s hyam")
print(f"Vowels={vowels}, Consonants={consonants}")


# Now, Count Occurence of each character 

def count_occuren(s):
    d={}
    for ch in s:
        if ch in d:
            d[ch]+=1
        else:
            d[ch]=1
    return d
print(count_occuren("hsadfuhlyyytt"))


# We can also use get() of dictionary to accessing items in dictionary
def count_freq(s):
    dct={}
    for ch in s:
        dct[ch]=dct.get(ch,0)+1
    return dct 
print(count_freq("bsadhhhhhtyuii"))  

# Find the high frequency character with its frequency

def max_freq(s):
    dtc={}
    for ch in s:
        dtc[ch]=dtc.get(ch,0)+1
    max_char=None
    max_count=0
    for char,count in dtc.items():
        if count>max_count:
            max_count=count
            max_char=char
    return max_count , max_char

a , b =max_freq("kjdsfhyuwfqhdsf")
print(f"Max Occurence={a} and Max_character={b}")


# Find non repeating character in string

def no_rep_char(s):
    dic={}
    for ch in s:
        dic[ch]=dic.get(ch,0)+1
    for ch in s:
        if dic[ch]==1:
            return ch
    return None
print(no_rep_char("SSdffgtr"))



    
