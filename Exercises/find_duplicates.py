# Find all duplicate characters.
def find_duplicate(s):
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    duplicates=set()
    for char,count in freq.items():
        if count>1:
            duplicates.add(char)
    return duplicates
print(find_duplicate("The famous great warrior of Italy"))

## Using set only:
def duplicate_find(s):
    dupl=set()
    uniq=set()
    for ch in s:
        if ch not in uniq:
            uniq.add(ch)
        else:
            dupl.add(ch)
    return dupl


## Remove duplicate characters(Kepp Order)


def duplicate_remove(s):
    seen=set()
    result=[]
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return "".join(result)