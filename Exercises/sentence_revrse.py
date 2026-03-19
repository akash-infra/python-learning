# Reverse words in a senetence

def reverse_word(s):
    words=s.split()
    return " ".join(words[::-1])

#another method:
def reverse_word(s):
    words_lst=[]
    for item in s.split():
        words_lst.append(item)
    return "".join(words_lst[::-1])

# So, mostly i have to create a list of words for these general solution::

#**************************************************************************************************

# Solution without built-In::

def reversed_words(s):
    current=""
    word_lst=[]
    result=""
    for ch in s:
        if ch!=" ":
            current+=ch
        else:
            if current!= "":
                word_lst.append(current)
            current=""
    # For last word:
    if current!= "":
        word_lst.append(current)
    # Reversing Manually:
    for i in range(len(word_lst)-1,-1,-1):
        result+=word_lst[i]
        if i!=0:
            result+=" "   # After adding one word from list to result we need space untill i=0
    return result


#************************************************************************************

# Reverse each word in a senetence

def each_word_reverse(s):
    current=""
    temp_lst=[]
    for ch in s:
        if ch!=" ":
            current=ch+current
        else:
            if current:
                temp_lst.append(current)
            current=""
    # checking last word:
    if current:
        temp_lst.append(current)
    # Adding list to resut
    return " ".join(temp_lst)
    








     