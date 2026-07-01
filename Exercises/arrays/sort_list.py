# Sort list/array  without using .sort() method in python


#*******************************************************************************************************


#Remeber-lists are mutable-->you can modify list without nedding to create a new list

def sort_lst(l):
    for i in range(len(l)):
        for j in range((i+1),len(l)):
            if l[j]>l[i]:
                l[i],l[j]=l[j],l[i]      # Here, tuple swapping works but this->l[i]=l[j]-->Overwrites/loose the original value
    return l
print(sort_lst([4,8,2,6,1,9,3,5,7]))