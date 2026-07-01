# Replcing a charcater without using .replace()

def char_replace(s,old_char,new_char):
    new_str=""    # New string becuase Strings are immutable.
    for ch in s:
        if ch == old_char:    # For case-insensitive=> if ch.lower()==old_char.lower()
            ch=new_char
            new_str+=ch
        else:
            new_str+=ch       
   
    return new_str

print(char_replace("The famous Bruce Sharma",'B','A'))

## This give (+=)  O(n*2) complexity in worst case which is not good.

## Optimal Solution:

def replace_char(s,old,new):
    result=[]
    for ch in s:
        if ch == old:
            result.append(new)
        else:
            result.append[ch]
    return "".join(result)

