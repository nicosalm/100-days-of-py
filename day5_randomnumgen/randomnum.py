# random number generator
import random

print("Welcome to the PyPassword Generator!")

# given a number of letters, symbols and numbers, generate a random password
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pwd = ""

uppercase_count = random.randint(1, nr_letters) # at least one uppercase letter
lowercase_count = nr_letters - uppercase_count  # the rest are lowercase

# generate ascii characters for random letters (both upper and lower case)
for i in range(0, uppercase_count):
    pwd += chr(random.randint(65, 90))

for i in range(0, lowercase_count):
    pwd += chr(random.randint(97, 122))
    
# generate a random symbol
for i in range(0, nr_symbols):
    pwd += chr(random.randint(33, 47))
    
# generate a random number
for i in range(0, nr_numbers):
    pwd += chr(random.randint(48, 57))

# shuffle the password
pwd = list(pwd)
random.shuffle(pwd)
pwd = "".join(pwd)

print(f"Your secure password is: {pwd}.")