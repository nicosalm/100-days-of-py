# dictionary examples
dictionary = {1 : "one", 
              2 : "two", 
              3 : "three"}

print(dictionary)

# access a value
print(dictionary[1])

# add / change a key-value pair
dictionary[4] = "four" # dictionary[key] = value
 
# remove a key-value pair
del dictionary[4] # del dictionary[key]

# iterate over a dictionary 
for key in dictionary:
    print(key, dictionary[key])
    
# iterate over a dictionary's keys
for key in dictionary.keys():
    print(key)
    
# iterate over a dictionary's values
for value in dictionary.values():
    print(value)
    
# iterate over a dictionary's key-value pairs
for key, value in dictionary.items():
    print(key, value)
    
# check if a key is in a dictionary
if 1 in dictionary:
    print("1 is in the dictionary")
    
# check if a value is in a dictionary
if "one" in dictionary.values():
    print("one is in the dictionary")
    
# check if a key is not in a dictionary
if 5 not in dictionary:
    print("5 is not in the dictionary")
    
# nesting dictionaries
travel_log = [
    {
        "country": "France", 
        "visits": 12, 
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany", 
        "visits": 5, 
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]