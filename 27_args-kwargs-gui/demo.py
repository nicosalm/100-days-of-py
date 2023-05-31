''' 
    *args and **kwargs allow you to pass a variable number of arguments to a function.
'''

def print_args(*args):
    for arg in args:
        print(arg)
        
# print_args('hello', 'world', '!')

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
        
# print_kwargs(a='hello', b='world', c='!')