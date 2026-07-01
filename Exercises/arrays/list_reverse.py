#Reverse a List without Slicing
def lst_reverse(l):
    result_lst=[]
    for i in range(len(l)-1,-1,-1): # range(start,end,steps)--->start is included,however,end-index is excluded that's why -1
     #   result_lst+=l[i]                ----------> Does'nt work because Only String can be concatated
        result_lst.append(l[i])
    return result_lst
print(lst_reverse(["akash","Ram","Shyam"]))

## Using Two-Pointer (In-Place):

def reverse_lst(l):
    left=0
    right=len(l)-1
    while left<right:
        # l[left]=l[right]
        # l[right]=l[left]      These steps does'nt work because it assigns ,and original value is lost
        #                       List becomes -->  ['Shyam', 'Ram', 'Shyam']

# Correct Way:-
        temp=l[left]
        l[left]=l[right]
        l[right]=temp
# For above: Python shortcut:-Tuple Swapping
        l[left],l[right]=l[right],l[left]
                        
        left+=1
        right-=1
    return l
print(reverse_lst(["akash","Ram","Shyam"]))




