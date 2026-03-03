# Second most frequent character in string

def second_most_freq_char(s):
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    unique_counts=sorted(set(freq.values()),reverse=True)
    if len(unique_counts) < 2:
        return None
    second_max=unique_counts[1]     # Because index stars from 0,1,2,3,4,5,6.....
    second_char=[char for char,count in freq.items() if count==second_max]
    return second_max,second_char
print(second_most_freq_char("Killssdfianfijqewhff8uqiewjfknureinuerdrwfewruderj"))   

# Lowest frequent character in string

def high_freq_char(s):
    dct={}
    for ch in s:
        if ch not in dct:
            dct[ch]=dct.get(ch,0)+1
    min_count=float('inf')
    min_char=None
    for char,count in dct.items():
        if count<min_count:
            min_count=count
            min_char=char

    return mx_char,mx_count

    