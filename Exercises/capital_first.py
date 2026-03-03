#Question:  Convert First Letter of Each Word to Capital without using title()  

def capitaliza_first_word(s):

# First Method:  
    # is_first_letter=True
    # result=""
    # for ch in s:
    #     if ch !=" " and is_first_letter :
    #         result+=ch.upper()
    #         is_first=False
    #     else:
    #          result+=ch
    #          if ch == " ":
    #             is_first_letter=True
    # return result

# Second Method:Using split() and join()
    # words=s.split()
    # new_list=[]
    # for word in words:
    #     new_list.append(word.capitalize()) 
    # return " ".join(new_list)

# Third method: Using List comprehension

 return " ".join(word.capitalize() for word in s.split())



    
 

print(capitaliza_first_word("reven in the sky"))



## Question02: Count words in a senetence

def count_words(s):
    count=0
    in_word=False
    for ch in s:
        if ch != " " and not in_word:
            count+=1
            in_word=True
        elif ch == " ":
            in_word=False
    return count
print(count_words("My name is virat from songra"))








