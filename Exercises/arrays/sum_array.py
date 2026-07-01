# Find Sum of all elements of Array:

def array_sum(l):
    result=int()
    i=0
    while i<len(l):
        result=result+l[i]
        i+=1
    return result
print(array_sum([1,2,3,4,5]))

# Using Fo loop::

def sum_of_array(l):
    if not l:
        return 0
    result=0
    for i in range(len(l)):
        result+=l[i]
    return result

# *******************************************************************************************************

# Find average of elements: Optimized Version
def array_average(l):
    if not l:
        return 0
    sum=0
    count=0
    for item in l:
        if isinstance(item,(int,float)):
            sum+=item
            count+=1
    return sum/count if count !=0 else 0

    
   

    