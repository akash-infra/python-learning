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

# General Solution
def long_word(s):
    word_lst=[]
    empty_dct={}
    for item in s.split():
        empty_dct[item]=len(item)
    longest_length=0
    longest_word=None
    for word,length in empty_dct.items():
        if length>longest_length:
            longest_length=length
            longest_word=word
    return longest_word,longest_length
print(long_word("The writer wants to write"))

# Withou using split():

def long_est_word(s):
    longest=""
    max_len=0
    current=""
    for ch in s:
        if ch!=" ":
            current+=ch
        else:
            if len(current)>max_len:
                max_len=len(current)
                longest=current
            current=""           # reset current for next word
            
         # Checking the Last word   because it does not end with space thus will not enter into else block    

    if len(current)>max_len:
        longest=current
        max_len=len(current)
    return longest,max_len



