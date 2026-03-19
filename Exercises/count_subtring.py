# Count Subtring Occurence (Overllaping allowed)
def count_subtring(s,sub):
    count=0
    for i in range(len(s)-len(sub)+1):  # How many positions a sub can fit into
        if s[i:i+len(sub)]==sub:       # TO match sub-->Slice the string from every ith index-->equql to sub
            count+=1
    return count
print(count_subtring("banananaa","nan"))

## My own striked solution

def subtring_count(s,sub):
    sub_str_lst=[]
    count=0
    for i in range(len(s)-len(sub)+1):    # Only range(len(s)-1)--->It creates invalid subtring in list from last 7:10
        sub_str_lst.append(s[i:i+len(sub)])
    for word in sub_str_lst:
        if word==sub:
            count+=1
    return count
print(subtring_count("banananaa","nan"))

## Using built-in startswith() method:
def count_sub(s,sub):
    count=0
    for i in range(len(s)-len(sub)+1):
        if s.startswith(sub,i):       # startswith(prefix,start,end)--->returns True or False
            count+=1
    return count

## Using find(prefix,start,end)---->returns  position where substr was founf --->returns -1 if not found
              # it is same as index()-->but this index() raises exception if not found

def count_sub_occurence(s,sub):
    count=0
    start=0
    while True:
        pos=s.find(sub,start)
        if pos==-1:               # If not found then find() will return -1
            break
        count+=1
        start=pos+1            # Now,start from next index ,move one step -allow overllaping
    return count