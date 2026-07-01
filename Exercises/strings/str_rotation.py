# Check if one string is rotation of another 

## If you can move some characters from the front to the end (or vice versa) in any one string,then you get other string.
## "abcde"    <---> "cdeab"
## Rotation=Circular-shift

def check_rotation(s1,s2):
    # length check first:
    if len(s1)!=len(s2):
        return False
    # Creating a doubled string because string rotation is about moving charcters from front to end
    # Circular Shift= ALways hidden inside doubled string.
    temp_str=s1+s1
    # Manually searching s2 inside the temp_str
    for i in range(len(temp_str)-len(s2)+1):
        match=True
        for j in range(len(s2)):
            if temp_str[i+j]!=s2[j]:
                match=False
                break
        if match:
            return True
    return False

