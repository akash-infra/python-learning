#  13. Swap Keys and Values in Dictionary.  

temp_dict={
    "name":"Akash",
    "PIN":212121
}

# for key in list(temp_dict.copy()): 
#        c=temp_dict[key]
#        temp_dict[c]=key
# print(temp_dict)
# gm hilosig hi ksid ,kl  kzkfj kdifj 
# 

swapped_dict={} 
for key in temp_dict:
    value=temp_dict[key]
    swapped_dict[value]=key
print(swapped_dict)

# Using Dixtionary Comprehension:

swap_dict={value: key for key,value in temp_dict.items()}
print(swap_dict)
