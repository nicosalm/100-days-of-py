'''
    Demo of list and dictionary comprehensions
'''

# create a list of numbers
numbers = [1, 2, 3, 4, 5]

# create a list of numbers squared
squares = [number ** 2 for number in numbers]
# print(squares)
 
 
# create a list of numbers squared if the number is even
squares = [number ** 2 for number in numbers if number % 2 == 0]
# print(squares)

'''
    The utility of list comprehensions is that they can be used to create lists
    from other lists, dictionaries, or other iterables.
    
    It's a shorter way of writing a for loop that appends to a list.
'''

# united states capitals dictionary
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock'}
# only print the capitals that start with the letter 'M' using comprehensions
capitals_starting_with_m = [capitals[state] for state in capitals if capitals[state].startswith('M')]
# print(capitals_starting_with_m)