# Check if the list is palindrome or not?
 # For example: [1,2,3,2,1]   ---> Palindrome
# [1,2,3,4,5]  -----> Nor Palindrome

def is_list_palindrome(l):
    left=0
    right=len(l)-1
    while left<right:
        if l[left]!=l[right]:
            return False
        left+=1
        right-=1
    return True
print(is_list_palindrome([1,2,3,2,1]))



