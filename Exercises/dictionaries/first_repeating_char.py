# Find first non-repeating character in a string:

s = "aabbcdeff"

freq_dict={}

for char in s:
    if char not in freq_dict:
        freq_dict[char]=1
    else:
        freq_dict[char]+=1
for char in s:
    if freq_dict[char]==1:
        print("First non-repeating Character:",char)
        break

# Instead of thinking "Which keys in dictionary are one?"
# Think: Which Charcater in Original string has freq 1 first?
