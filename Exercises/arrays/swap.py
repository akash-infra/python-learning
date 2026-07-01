# Swap first and last element of array/list:

def swap_first_last(l):
    if len(l)<2:
        return l
    temp=l[0]
    l[0]=l[-1]
    l[-1]=temp
    return l

print(swap_first_last([1,2,3,4,5]))
    