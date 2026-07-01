# Find Common Elements in two Lists

def find_common(l1,l2):
    result=[]
    for item in l1:
        if item not in result:
         for elem_ent in l2:
            if elem_ent not in result:
             if item==elem_ent:
                result.append(item)
    return result

print(find_common(["Akash",1,2,4,"Vikash"],[9,"Akash",2,"Gaurav"]))

# ## More Efficient:
# def find_common(l1,l2):
#    result=[]
#    for item in l1:
#       if item in l2 and item not in result:
#          result.append(item)
#    return result

# ## Optimized Version (Using Set for lookup Only):
# def common_element(l1,l2):
#    result=[]
#    s2=set(l2)
#    for item in l1:
#       if item in s2 and item not in result:
#          result.append(item)
#    return result
      

