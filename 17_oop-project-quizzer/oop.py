"""
    Review of OOP concepts
"""

# 1. Class
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"


# 2. Instance
dog = Dog("Rex")

# 3. Method
dog.speak()  # "Rex says woof!"

# 4. Attribute/Property
dog.name  # "Rex"

# 5. Class variable
class Dog:
    species = "Canis familiaris" # Class variable, a static variable common to all instances of a class

    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return self.name + " says woof! He is a " + self.species
    
# 6. Instance variable
class Dog:
    def __init__(self, name):
        self.name = name
        self._age = 0 # Instance variable, a variable that is unique to each instance

    def speak(self):
        return self.name + " says woof!"
    
    def get_age(self): # Getter
        return self._age
    
    def set_age(self, age): # Setter
        self._age = age

# 7. Inheritance
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def speak(self):
        return self.name + " says " + self.sound()
    
    def sound(self):
        pass
     
class Dog(Animal):
    def sound(self):
        return "woof!"
     
# test 
dog = Dog("Rex", "Canis familiaris")
dog.speak() # "Rex says woof!"
 
# 8. Encapsulation
class Dog:
    def __init__(self, name):
        self._name = name # Encapsulated variable, a variable that is hidden from other classes
        
    def speak(self):
        return self._name + " says woof!"
    
    def get_name(self): # Getter
        return self._name
    
    def set_name(self, name): # Setter
        self._name = name
        
# test
dog = Dog("Rex")
dog.get_name() # "Rex"