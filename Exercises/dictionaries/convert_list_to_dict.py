# Convert two List to Dictionary

keys = ["name", "age", "course", "city"]

values = ["Akash", 24, "MCA", "Ghaziabad"]

list_dict={}

# Using loops
if len(keys)==len(values):
    for i in range(len(keys)):
        list_dict[keys[i]]=values[i]
    
print(list_dict)
