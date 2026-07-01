#**************Find all duplicate elements in a list

def find_dupl(l):
    duplicates=set()
    count_freq={}
    for x in l:
        if x not in count_freq:
            count_freq[x]=1
        else:
            count_freq[x]+=1 
    for element in count_freq:
        if count_freq[element]>1:
            duplicates.add(element)
    return duplicates

print("Duplicate Elements in the List are:",find_dupl([1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1]))
    