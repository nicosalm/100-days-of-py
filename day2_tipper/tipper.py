''' Day 2 Tipper'''

# – Mathematical operators

# int, float, and complex data types can be used with the following operators: +, -, *, /, //, %, **
num = 2
# complex operations 
num = num ** (2 + 1) * 2 - 15 / 3 + 1 # 12.0
mod = 15 % 2 # 1

# – String splicing and formatting1

# We can splice strings using square brackets
string = "Hello World!"
string = string[0:5] # "Hello"
string = string[6:] # "World!"

string = "Hello World!"
string = string[::-1] # !dlroW olleH

# We can also use the format() method to insert variables into strings
name = "Nico"
place = "Earth"
formatted_string = "Hello, my name is {} and I'm from {}.".format(name, place)

# We can also use the f-string method to insert variables into strings
tax_bracket = "middle"
amount = 10000
formatted_string = f"I am in the {tax_bracket} class and I make ${amount} a year."

# Also we can use .upper() and .lower() to change the case of a string
string = "Hello World!"
string = string.upper() # "HELLO WORLD!"

# We can also use .title() to capitalize the first letter of each word in a string
string = "hello world!"
string = string.title() # "Hello World!"

# – Now, let's use what we've learned to create a tip calculator!


print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? %"))
    
def tip_calculator(bill, tip):
    return bill * (tip / 100)
    
total_bill = round(bill + tip_calculator(bill, tip), 2)
print(f"Your total bill is ${total_bill}.")

# Now, let's add a feature to split the bill between multiple people
people = int(input("How many people to split the bill? "))
if people == 1: 
    print(f"Your total bill is ${total_bill}.") # no need to split the bill
print(f"Each person should pay ${round(total_bill / people, 2)}.")

# we can expand this program to include a split bill feature
# we can also add a while loop to make sure the user enters a valid input
