"""Demo of scope in Python.
"""

def f():
    """Prints the value of x.
    """
    print(x)
    
x = 5

f()

# This will throw an error because x is not defined in the scope of the function

