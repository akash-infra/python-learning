# Find Longest word in a sentence OR  find longest substring in a string.

# My own solution:

def longest_word(s):


    list1=[]
    for word in s.split():
        list1.append(word)
    

    l_dict={}
    for w in list1:
        l_dict[w]=l_dict.get(w,0) + len(w)
    
    sub_string=None
    lon_length=0
    for substr,length in l_dict.items():
        if length>lon_length:
            lon_length=length
            sub_string=substr 

    return sub_string,lon_length
print(longest_word("ajfbda th ysd lads nadsjgnajgbdsgbdsal"))


# Modifid Solution

def longest_substring(s):
    max_length=0
    max_sub_string=""
    for word in s.split():
        if len(word)>max_length:
            max_length=len(word)
            max_sub_string=word
    return max_sub_string,max_length
print(longest_word("ajfbda th ysd lads nadsjgnajgbdsgbdsal"))

