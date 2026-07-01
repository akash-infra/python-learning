# 12.Create a Dictionary Using dictionary comprehension

#*************************Method 01

# Using fromkeys() method

empt_dict={

}
d=dict.fromkeys(range(5),"Akash")
#empt_dict.fromkeys(range(4),"LaLa") ---->Temporary dictionary was created and them Lost
#print(empt_dict)
print(d)
# however,
new_dict=empt_dict.fromkeys(range(4),"LaLa")  # But here, dictionary Was stored 
print(new_dict)


# fromkeys() DOES NOT modify the original dictioanary , it CREATES a new dictioanry.It does not do IN+-PLACE modification


# Interview Trap :
c=dict.fromkeys(range(3),[])
print(c)
c[0].append(1)
print(c)  # {0:[1],1:[1],2:[1]} ---->WHY WHY WHY , why this happens, Only 0th index key-value must be updated
# Because Here all keys(0,1,2) points to ----> same list object []

# Thats why safer Version:
e={i: [] for i in range(5)}
print(e)
e[1].append(99)
print(e)
# Now , only each key gets seperate list.


# *************************************** Method 02:
# Using Dictionary Comprehension

sq_dict={x:x**2 for x in range(1,6)}
print(sq_dict)

filter_dict={x:"even" if  x%2==0 else "odd" for x in range(1,21)}
print(filter_dict)

text="engineering"
text_dict={} 
for char in text:
    text_dict[char]=text_dict.get(char,0)+1
# Same thing with dictionary comprehension

count_dict={char:text.count(char) for char in text}
print(count_dict) 
