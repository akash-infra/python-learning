# Now, Remove a Specific Character from string.

# Note: we know strings are immutable

def remove_char(s,char):
    result=""
    for ch in s:
        if ch!=char:
            result+=ch
    return result
  #return "".join(ch for ch in s if ch!=char)   ====> More clean,short,optimized

## Oprtimal Solution

def rem_char(s,char):
    result=[]
    for ch in s:
        if ch != char:
            result.append(ch)
    return "".join(result)


## Remove Only first Occurences::

def remove_first_char(s,char):
    result=[]
    removed=False
    for ch in s:
        if ch==char and not removed:
            removed=True
            continue
        result.append(ch)
    return "".join(result)

## Removing Multiple Characters:
def remove_multiple_char(s,chars):
    chars=set(chars)
    return "".join(ch for ch in s if ch not in chars)
        
        