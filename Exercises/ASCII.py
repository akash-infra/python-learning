# Find ASCII value of each character

def get_ascii_value(s):
    result=[]
    for ch in s:
        result.append((ch,ord(ch)))
    return result
print(get_ascii_value("Akash"))

## Formatted Output:

str=input("enter a string: ")
for ch in str:
    print(f"Character:{ch} | ASCII: {ord(ch)}")
