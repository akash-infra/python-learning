# Find second largest element in array without using .sort()



#**************************************************************************************************

# But we do not need sorting for finding second large element:

def second_large(l):
    first=float('-inf')  # "first" is negative infinity--->Represents - smaller than any number
    second=float('-inf')
    for num in l:
        if num>first:
            second=first
            first=num
# if num is not greater than first then first remains max,and second remains second max:
# But it is possible that num could be greater than second-->
# however, num shouldn't be the repeatition of first then---->
        elif num>second and num!=first:  # Will be checked when if-condition is false
            second = num
    return second



# *******************************************************************************************************

# Find second Minimum element in array

def second_min(l):
    first=float('inf')     # "first" is positive infinity--->Bigger then any number
    second=float('inf')
    for num in l:
        if num<first:
            second=first
            first=num
        elif num<second and num!=first:
            second=num
    return second

# For mixed data ,we can use isinstance()  method and then can write same logic.

        


