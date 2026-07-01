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
