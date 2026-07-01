# 14. Find the maximum Value in Dictionary
marks = {
    "Math": 78,
    "Science": 92,
    "English": 85,
    "Computer": 95,
    "History": 88
}
max_value=0
max_sub=None
for x in marks:
    if marks[x]>max_value:
        max_value=marks[x]
        max_sub=x
print(max_sub,max_value) 
