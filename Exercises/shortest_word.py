# Find a shortest word in a sentence:

# General Solution:

def shortest_word(s):
    min_len=float('inf')
    shortest= ""
    for word in s.split():
        if len(word)<min_len:
            min_len=len(word)
            shortest=word
    return shortest,min_len
print(shortest_word("The guy is handsome"))

## Solution without .spli():

def shortest_substr(s):
    shortest= ""
    min_len=float('inf')
    current_shortest= ""
    for ch in s:
        if ch!=" ":
            current_shortest+=ch
        else:    # It means word is ended and check if its the shortest
            if len(current_shortest)<min_len:
                min_len=len(current_shortest)
                shortest=current_shortest
            current_shortest=""         # Ready for the next word
     # Checking the Last word   because it does not end with space thus will not enter into else block    
    if len(current_shortest)<min_len:
      min_len=len(current_shortest)
      shortest=current_shortest
    return shortest,min_len
    