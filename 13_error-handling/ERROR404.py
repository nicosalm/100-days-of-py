""" Error handling """

try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
    
except ZeroDivisionError:
    print("Age cannot be 0.")
    
except ValueError:
    print("Invalid value")
    
    
# Catching all errors
except Exception:
    print("Something went wrong. You should not see this.")
    
# –––––––––––––––––––– #
# Raising errors
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error) # prints the error message
    
# –––––––––––––––––––– #
# Custom errors
class TooManyPagesReadError(ValueError):
    pass

class Book:
    def __init__(self, name:str, page_count:int):
        raise TooManyPagesReadError("You have read too many pages.")
    
try:
    book = Book("Harry Potter", 400)
except TooManyPagesReadError as error:
    print(error)