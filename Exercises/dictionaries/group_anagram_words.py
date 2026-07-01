# Group words which are anagram:
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagram_dict={}
for element in words:
    key="".join(sorted(element))
    
    if key not in anagram_dict:
        anagram_dict[key].append(element)
    else:
        anagram_dict[key]=[element]
    
print(anagram_dict)
        

