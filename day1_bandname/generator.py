print("\n#####   Welcome to the Band Name Generator!   #####")

# intake a city name
city = input("What's name of the city you grew up in?\n")

# if the user enters erronious input, the program should ask for the input again
while all(x.isalpha() or x.isspace() for x in city) == False:
    city = input("Please enter a valid city name.\n")
    
    # what just happened? 
    # - the function all() takes an iterable and returns True if all elements are True
    # - the function isalpha() returns True if all characters in the string are alphabetic and there is at least one character, False otherwise
    # - the function isspace() returns True if there are only whitespace characters in the string and there is at least one character, False otherwise
    # - we check if all characters in the string are alphabetic OR whitespace, if not, we ask for the input again
    
# now, intake an animal name
   
animal = input("What's your favorite animal?\n")

while all(x.isalpha() or x.isspace() for x in animal) == False:
    animal = input("Please enter a valid animal name.\n")
    
# print the band name to the console!
print("Your band name could be the " + city + " " + animal + "s!")