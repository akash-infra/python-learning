# Merge two Lists 

# def merge_lists(l1,l2):
#     result=[]
#     for i in range(len(l1)):
#         result.append(l1[i])

#     for j in range(len(l2)):
#         result.append(l2[j])
    
#     return result

##  merge two sorted lists :  

def merge_sorted(l1,l2):
    result=[]
    i=j=0
    while i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            result.append(l1[i])
            i+=1
        else:
            result.append(l2[j])
            j+=1
    while i<len(l1):
        result.append(l1[i])
        i+=1
    while j<len(l2):
        result.append(l2[j])
        j+=1
    return result

print(merge_sorted([1,2,4,6,8,],[9,7,5,3,1]))


