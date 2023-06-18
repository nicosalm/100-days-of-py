'''
Format:
try:
    # the code that may cause an error
except:
    # the code that will run if the error occurs
else:
    # the code that will run if there is no error
finally:
    # the code that will run no matter what
'''

# file not found error
with open("a_file.txt") as file:
    file.read()
    # print("File was found.
    # raise FileNotFoundError, no such file or directory: 'a_file.txt'
    
# key error
a_dictionary = {"key": "value"}
# KeyError: 'non_existent_key'
value = a_dictionary["non_existent_key"]

# index error
fruit_list = ["Apple", "Banana", "Pear"]
# IndexError: list index out of range
fruit = fruit_list[3]


# type error
text = "abc"
# TypeError: can only concatenate str (not "int") to str
print(text + 5)

# handling errors
# try except
try:
    # the code that may cause an error
    file = open("a_file.txt")
    
except FileNotFoundError:
    # the code that will run if the error occurs
    print("There was an error")

# and you can have multiple except blocks
try:
#    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["non_existent_key"])
    
except FileNotFoundError:
    # the code that will run if the error occurs
    file = open("a_file.txt", "w")
    
except KeyError as error_message:
    # the code that will run if the error occurs
    print(f"The key {error_message} does not exist.")
    
else:
    # the code that will run if there is no error
    content = file.read()
    
finally:
    # the code that will run no matter what
    file.close()
    print("File was closed.")
    
''' 
    raise your own errors
'''
# raise keyword
height = float(input("Height: "))
if height > 3:
    # create your own error
    raise ValueError("Human height should not be over 3 meters.")

# create your own error
def add(n1, n2):
    if type(n1) is not int or type(n2) is not int:
        raise TypeError("n1 and n2 must be integers.")
    return n1 + n2