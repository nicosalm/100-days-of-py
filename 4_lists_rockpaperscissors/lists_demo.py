# import Dictionary and List
from typing import Dict, List

# demo of list
def list_demo():
    
    # create a list
    our_list = [1, 2, 3, 4, 5]
    
    # – printing the list in different ways
    print("\nprinting the list in different ways:")
    
    # print the list
    print(our_list)
    
    # print the element at index 0
    print(our_list[0])
    
    # print the list in reverse order
    print(our_list[::-1])
    
    # – different ways to traverse the list
    print("\ndifferent ways to traverse the list:")
    
    # traverse the list and print each element
    for i in range(len(our_list)):
        print(our_list[i], end=" ")
        
    # traverse the list and print each element
    for i in our_list:
        print(i)
        
    # enumerate returns a tuple (i, j)
    for i in enumerate(our_list):
        print(i)
        
    # enumerate returns a tuple (i, j)
    for i, j in enumerate(our_list):
        print(i, j)
        
    # the two for loops above are different in the following way:
    # the first for loop returns a tuple (i, j)
    # the second for loop returns two variables i and j
        
    # – list comprehensions
    print("\nlist comprehensions:")    
    
    # list comprehension
    our_list = [i for i in range(10)]
    print(our_list)
    # this is equivalent to the following code block:
    # our_list = []
    # for i in range(10):
    #     our_list.append(i)
    # print(our_list)
    
    # list comprehension with condition
    our_list = [i for i in range(10) if i % 2 == 0]
    print(our_list)
    # this is equivalent to the following code block:
    # our_list = []
    # for i in range(10):
    #     if i % 2 == 0:
    #         our_list.append(i)
    # print(our_list)
    
    # list comprehension with condition
    our_list = [i if i % 2 == 0 else 0 for i in range(10)]
    print(our_list)
    # this is equivalent to the following code block:
    # our_list = []
    # for i in range(10):
    #     if i % 2 == 0:
    #         our_list.append(i)
    #     else:
    #         our_list.append(0)
    # print(our_list)
    
def dict_demo():
    # create a dictionary
    our_dict = {"a": 1, "b": 2, "c": 3}
    
    # – printing the dictionary in different ways
    print("\nprinting the dictionary in different ways:")

    # print the dictionary
    print(our_dict)
    
    # print the value of key "a"
    print(our_dict["a"])
    
    # print the keys of the dictionary
    print(our_dict.keys())
    
    # print the values of the dictionary
    print(our_dict.values())
    
    # – different ways to traverse the dictionary
    print("\ndifferent ways to traverse the dictionary:")

    # traverse the dictionary and print each key and value
    for i in our_dict:
        print(i, our_dict[i], end=", " if i != "c" else "\n")

    # traverse the dictionary and print each key and value
    for i in our_dict.keys():
        print(i, our_dict[i], end=", " if i != "c" else "\n")
        
    # traverse the dictionary and print each key and value
    for i in our_dict.values():
        print(i, end=", " if i != 3 else "\n")
        
    # traverse the dictionary and print each key and value
    for i, j in our_dict.items():
        print(i, j, end=", " if i != "c" else "\n")
        
    # – dictionary comprehensions
    print("\ndictionary comprehensions:")

    # dictionary comprehension
    our_dict = {i: i * i for i in range(10)}
    
    # this is equivalent to the following code block:
    # our_dict = {}
    # for i in range(10):
    #     our_dict[i] = i * i
    print(our_dict)

if __name__ == "__main__":
    list_demo()
    # dict_demo()