# Move All zeros to end in the Array/List:

def move_zeros(l):
    end=len(l)-1
    i=0
    while i<len(l):
        if l[i]==0 and l[end]!=0:
            l[i],l[end]=l[end],l[i]
            end-=1
        else:
            i+=1
    return l
print(move_zeros([1,0,5,0,6,7,0,0,9,8,4]))  

## More Optimized version

def move_zeros(l):
    pos = 0
    
    for i in range(len(l)):
        if l[i] != 0:
            l[pos], l[i] = l[i], l[pos]
            pos += 1
    
    return l


