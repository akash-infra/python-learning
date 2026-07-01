# Find length of array without using length.
def len_of_lst(l):
    length=0
    for item in l:
        length+=1
    return length
print(len_of_lst([1,"Gaurav","2",2,6]))


# Remove a specific element:
def remove_element(lst,ele_ment):
    for item in lst:
        if item==ele_ment:
            del item
        else:
            continue
    return 

