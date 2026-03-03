# Count words in a sentance

string= "Hey! My name is Akash Sharma"

# > Then each word is sperated by spaces 

lst=string.split( )
print(lst)
print(f"Word Count in String is {len(lst)}")  

# Without using Build in function

def count_word(s):
    count=0
    in_word=False
    for ch in s:
        if ch != " " and not in_word:       # We just encountered the word and we were not already inside the word.
            count=+1
            in_word=True
        elif ch==" ":                       # We have found a space
            in_word=False                    # AND the word has just ended.We are no longer inside the word.
    return count 
print(count_word("Hey! this is Live Coding in python"))

# Above solution works fine in both test cases like ("Hello  word")  and ("  ")
# Because it ignore the multiple space. in_word Flag is doing all stuff.    



# Question: Reverse Words in a sentence?

# Using built in functions:

def reverse_sentence(s):
    reversed=""
    lst=s.split()
    # for i in range(len(s)-1,-1,-1):
    #     reversed+=lst[i]
    for word in lst:
        reversed=word+" "+reversed
    return reversed.strip()
print(reverse_sentence("Hii My name is Akash"))

#---> Another best solution for this

def reverse_the_sentence(s):
    words=s.split()
    return " ".join(words[::-1])






     





        
