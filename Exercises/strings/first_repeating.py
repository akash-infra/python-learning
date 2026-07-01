# Find first repeating character.

##-->It means that charcater which started repeating first from left to right.
def first_repeating(s):
  empty_set=set()
  for ch in s:
    if ch not in empty_set:
      empty_set.add(ch)
    else:
      return ch
  return None

## Using Dictionary:
def repeating_first(s):
  freq={}
  for ch in s:
    freq[ch]=freq.get(ch,0)+1
    if freq[ch]==2:
      return ch
  return None
    



    






