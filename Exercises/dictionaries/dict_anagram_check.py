# Check if two strings are anagram

# def find_anagram(s1,s2):
#     if len(s1)!=len(s2):
#         return False
#     first_set=set()
#     for x in s1.lower():
#         if x not in first_set:
#             first_set.add(x)
#     for y in s2.lower():
#         if y not in first_set:
#             return False
#     return True
# print(find_anagram("Listen","Silent")) 

#---> But above approach can not deal with repeating characters.

def are_anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    count_freq={}
    s1=s1.lower()
    s2=s2.lower()
    for ch in s1:
        if ch not in count_freq:
            count_freq[ch]=1
        else:
            count_freq[ch]+=1
    for ch in s2:
        if ch not in count_freq:
            return False
        count_freq[ch]-=1
    # Now, Every dict-value must have become "0" , for both strings to be anagram.
    for val in count_freq.values():
        if val != 0:
            return False
    return True

print(are_anagram("Listen","Silent")) 
