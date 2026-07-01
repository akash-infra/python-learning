# Count frequency of each element in List:

def count_frequency(l):
    freq_dict={}
    for item in l:
        freq_dict[item]=freq_dict.get(item,0)+1
            
    return freq_dict
print(count_frequency(["akash",1,3,"vikash",4,1,3,"akash"]))
