# Find Maximum and Minimum element in List



##01: When list contains only numbers:--->

#********************************************************************************************************
# def max_element(l):
#   #  max=0       # It is dangerous coz what if list also contains -ve elements
#     max=l[0]             #  We initialize max with first element to correctly handle negative values
#     for num in l:
#         if num>max:
#             max=num
#     return max
# print(max_element([1,2,3,4,5,89,0]))

#********************************************************

# def min_element(l):
#     min=l[0]
#     for num in l:
#         if num<min:
#             min=num
#     return min
# print(min_element([1,0,9,5,8,-1,6,3,2]))

#******************************************************************************************************* 

### Both together:

def min_max_element(l):
    max_value=l[0]
    min_value=l[0]
    for num in l:
        if num>max_value:
            max_value=num
        if num<min_value:
            min_value=num
    return max_value,min_value
print(min_max_element([1,0,9,5,8,-1,6,3,2,89,67,1]))



#“String comparison in Python is lexicographical, based on ASCII values, 
# comparing characters from left to right.”
print(min_max_element(["Akash","Vikash","Gaurav","akash","Zig"]))



#*************************************************************************************************

##02: When List contains both types of elements(str+numerical)::

def min_max_value(l):
    min_num=None
    max_num=None
    min_str=None
    max_str=None
    for item in l:
        if isinstance(item, int):
            if max_num is None or item>max_num:
                max_num=item
            if min_num is None or item<min_num:
                min_num=item
        elif isinstance(item,str):
            if max_str is None or item>max_str:
                max_str=item
            if min_str is None or item<min_str:
                min_str=item
    return min_num,max_num,min_str,max_str
print(min_max_value([3, "apple", 7, "banana", 1]))






            
    


