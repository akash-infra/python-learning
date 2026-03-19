#**************************************************************************************

#Question: Convert lowercase to uppercase without using inbuilt.

## Method01: using Helper String

def convert_to_upper(str):
    lower_cases="abcdefghijklmnopqrstuvwxyz"
    upper_cases="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result=""
    for ch in str:
        if ch in lower_cases:
            index_0f_char=lower_cases.index(ch)        # finding index of each
            result=result+upper_cases[index_0f_char]    # access the relative index uppercase
        else:
            result+=ch     # Keeping non-alphabetic as it is
    return result
print(convert_to_upper("ramayan@akash1"))

## Using ASCII Values with ord() and chr()


# ord() -----> To get the ASCII value   (a-z) = 97-122  (A-Z)= 65-90  | Difference each letter is 32
# chr() ------> To get the character from the ASCII value

def to_uppercase(input_str):
    result=""
    for ch in input_str:
        if 'a'<=ch<='z':     # Checking wheather the character is lower
            result+=chr(ord(ch)-32)
        else:
            # Keep non-alphabetics as they are
            result+=ch
    return result

print(to_uppercase("sharma1akash"))

def to_lowercase(str):
    result=""
    for ch in str:
        if 'A'<=ch<='Z': # Checking whether the characyter is Uppercase
            result+=chr(ord(ch)+32)
        else:
            result+=ch
    return result
print(to_lowercase("virat56Rahul@"))


### Swapcase/Toggle case program without upper() and lower()

def swap_cases(input_string):
    result=""
    for ch in input_string:
        if 'a'<=ch<='z':
            result+=chr(ord(ch)-32)
        elif 'A'<=ch<='Z':
            result+=chr(ord(ch)+32)
        else:
            result+=ch
    return result
print(swap_cases("heyveerTUMbadeChalo1998toTHE Top@"))




