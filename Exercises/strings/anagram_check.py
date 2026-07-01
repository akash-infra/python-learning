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



#----->Same element with same frequencies in both strings but with just different order.

def check_anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    dict1={}
    dict2={}
    for ch in s1:
        dict1[ch]=dict1.get(ch,0)+1
    for ch in s2:
        dict2[ch]=dict2.get(ch,0)+1
    if dict1!=dict2:
        return False
    return True

## Using One Dictionary::

def anagram_check(s1,s2):
    # If length is not same they never can be the anagram
    if len(s1)!=len(s2):
        return False
    freq={}
    # Count Characters from s1
    for ch in s1:
        freq[ch]=freq.get(ch,0)+1
    # Subtract using s2
    for char in s2:
        if char not in freq:
            return False
        freq[ch]-=1
        if freq[ch]<0:
            return False
    return True

# Group anagrams from list of strings::

# A list is given in which there are multiple words/strings , then group anagrams.

def group_anagrams(lst):
    # Creat a empty dictionary
    anagram_groups={}
    for word in lst:      # Loop through each strs/word in given list
        key="".join(sorted(word))     # Create a individual-sorted -key word for matching it to others anagram
        if key not in anagram_groups:
            anagram_groups[key]=[word] # Taking the same key-->looping next word2-->sorting word2--->If not in groups--->adding that word(value) as/in list to that key
        else:
            anagram_groups[key].append(word) # if sorted word in groups already then appending that to key's list
    return list(anagram_groups.values())   # Returning list of key's value
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
        
    
   


    
        

