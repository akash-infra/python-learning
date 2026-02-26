# Check If two strings are Anagrams?

# Anagram=Two strings that contain the same characters with the same frequency, but possibly in different order.

# 1. i need to know each character and 2.frequency of each charater
# If both matches, strings are anagram.abs

#def check_anagram():
s1="Hello"
s2="lleho"
    # empty_set1=set()
    # empty_set2=set()
    # for ch in s1:
    #     if ch not in empty_set1:
    #         empty_set1.add(ch)
    # for char in s2:
    #     if char not in empty_set2:
    #         empty_set2.add(char)
def check_anagram(s1,s2):
    d1={}
    d2={}
    for ch in s1:
        if ch in d1:
            d1[ch]+=1
        else:
            d1[ch]=1
    for char in s2:
        if char in d2:
            d2[char]+=1
        else:
            d2[char]=1
    if d1!=d2:
        return False
    return True

print(check_anagram("hello","llhoe"))
    
        

