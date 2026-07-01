# Remove duplicates from List/Array in python without using built-ins:

# def remove_duplicates_in_list(l):
#     is_repeating=False
#     current=""
#     empty_set=set()
#     for item in l:
#         if item not in empty_set:
#             empty_set.add(item)
#         else:
#             l.remove(item)

#*********************************************************************************
def remove_dupl_in_list(l):
    result=[]
    for i in range(len(l)):
        is_duplicate=False
     #   for j in range((i+1),len(l)):  ---------------->Does not works
        for j in range(len(result)):
            if l[i]==result[j]:
                is_duplicate=True
                break
        if is_duplicate==False:
            result.append(l[i])
    return result
print(remove_dupl_in_list(["akash","Vikash","Ram","akash","Ram"]))

#***********************************************************************************************
def remove_dupl_in_list(l):
    new_lst=[]
    for item in l:
        if item not in new_lst:
            new_lst.append(item)
            
    return new_lst

## More optimized version:

def remove_dupl_in_list(l):
    seen={}
    new_lst=[]
    for item in l:
        if item not in seen:
            seen[item]=True
            new_lst.append(item)
            
    return new_lst 


#***********************************************************************************************************************

# Modifying List in Place:
def remove_duplicates(l):
    i=0
    while i<len(l):
        j=i+1
        while j<len(l):
            if l[i]==l[j]:
                del l[j]  # j does not increases after deletion;avoida repeation
            else:
                j+=1

        i+=1
    return l
print(remove_duplicates(["akash","Vikash","Ram","akash","Ram"]))

  


