# Count Frequency of elements in a list

nums = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]
num_freq={}
#for i in range(len(nums)):
# for x in nums:
 #   num_freq[nums[i]]=num_freq.get(nums[i],0)+1
#    num_freq[x]=num_freq.get(x,0)+1
#print(num_freq)


# Without any dictionary Methods:
count=1
seen=set()
for i in range(len(nums)):
    if nums[i] not in seen:
        num_freq[nums[i]]=count
        seen.add(nums[i])
    else:
        num_freq[nums[i]]=num_freq[nums[i]]+1
       
print(num_freq)

## More Simpler and upgraded version:
num_freq={}
num

    

    
    


