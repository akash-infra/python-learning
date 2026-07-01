# Find length of string without using len()

def s_length(s):
    l=0
    for ch in s:
        if ch!=" ":              # To ignore spaces; if required only
            l+=1
    return l
print(s_length("Hii! my name is String"))