#****************************************** Loops ****************************************************************************

#1.while loops           2. for loop

#With while loop we can execute a set statements as long as the condition is true.
#while loop executes based on some condition.
#Use while loop when you do not know how many times loop should run.
i=1
while i<6:
    print(i)
    #increment/derement i ,or else the loop value continue forever.
    i+=1

# break :
# with the break statement we can stop the loop even if the while condition is true:
i=1
while i<6:
    print(i)
    if i== 3:
        break
    i+=1   
        
    
        
      # Position of break does matter.
      #after break loop stops and exit,no further evaluation happens.
     


#continue :
# with continue statement we can stop the current iteration,and can continue with the next.

i=0
while i < 6:
    i+=1
    if i==3:
        continue
    print(i)
else:
    print("Number is no longer than 6.")    

# else :
# Once the condition is false, it will be executed. 
# else block will not be executed if the loop is stopped by break.

####################### for loop :
# When yoy know how many times loop should run
# for loops needs and iteratble object to   iterate  
fruits=["apple", "banana","cherry"]
for x in fruits:
    print(x) 

    #The for loop does not require an indexing variable to set beforhand

# break :
# we ccan stop loop before it has  looped through all items
for x in fruits:
    print(x)
    if x=="banana":
        break
 # oR
for x in fruits:
    if x=="banana":
        break
    print(x)

# continue    ~ jump

for x in fruits:
    if x=="banana":
        continue
    print(x)

# The range() Function:
#returns sequence of number 0(default),increments by 1(default), ends at specified.
# range(6)-->0,1,2,3,4,5
# last index is excluded.
# However, range(1,30,3)----->It increament value by adding third parametre 3.

for x in range(6):
    print(x)             #prints 1-5
for y in range(1,30,4):
    print(y)            #prints 1,5,9,13,17,21,25,29
else:
    print("Loop has ended.")    

# else:
# Executes when loop is finished.but will not execute after break.
for x in range(6):
  if x == 3: break
  print(x)
else:                   # will not be executed.
  print("Finally finished!")
    
################################### Nested Loops:

#The "inner loop" will be executed one time for each iteration of the "outerloop":

s="*****" 
lst=["car","bus","tractor"]
for x in s:
    for y in range(len(lst)):
        print(lst[y])
       
           
