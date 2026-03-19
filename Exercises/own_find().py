# Implement you own find function

def my_find_func(s,sub):
    # positions=[]           -------------> For ALL Occurences
    for i in range(len(s)-len(sub)+1):
        if s[i:i+len(sub)]==sub:
            return i                #Returns where the first match is
        #   positions.append(i)
    return -1      
#   return positions             
print(my_find_func("loacalocalacala","cal"))

## Without slicing::  Naive String MAtching Algorithm

### IDEA BEHIND:: For every position i in string s, try to match the entire substring sub

def my_own_find(s,sub):
    # Try every starting position where sub can fit
    for i in range(len(s)-len(sub)+1):
        # Lets assume,position is completely match
        match=True
        #Compare each character of substring
        for j in range(len(sub)):
            # Compare main character in string with character in substring
            if s[i+j]!=sub[j]:  # If even ONE mismatch
                match=False     
                break       # Stop checking further
        if match:           #if FULL match found
            return i       # then reurn i
    return -1


