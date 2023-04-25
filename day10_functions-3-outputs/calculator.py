
"""
    A calculator which takes in two numbers and an operator and returns the result. The result is carried over into the next calculation.
"""
import math


def calculate(num1: float, operator: str, num2: float):
    
        calculating = True
        
        while calculating:
            print("Enter an operator (+, -, *, /, %, ^, log) or 'q' to quit: ")
            
            # use lambda functions to make the code more concise
            if operator == "+":
                funct = lambda x, y: x + y
                result = funct(num1, num2)     
                
            elif operator == "-":
                funct = lambda x, y: x - y
                result = funct(num1, num2)
                
            elif operator == "*":
                funct = lambda x, y: x * y
                result = funct(num1, num2)
                
            elif operator == "/":
                funct = lambda x, y: x / y
                result = funct(num1, num2)
                
            elif operator == "%" or operator == "mod":
                funct = lambda x, y: x % y
                result = funct(num1, num2)
                
            elif operator == "^":
                funct = lambda x, y: x ** y
                result = funct(num1, num2)
                
            elif operator == "log":
                funct = lambda x, y: math.log(y, x)
                result = funct(num1, num2)
                
            elif operator == "q":
                return
            
            else:
                print("Invalid operator.")
                return
            
            print(f"{num1} {operator} {num2} = {result}")
            
            continue_calculating = input("Continue operating with this result? (y/n): ")
            if continue_calculating == "y":
                num1 = result
                operator = input("Enter an operator (+, -, *, /, ^, log) or 'q' to quit: ")
                num2 = float(input("Enter another number: "))
                
            else:
                print(f"Quitting calculator. Final result: {result}")
                calculating = False

def main():
    
    num1 = float(input("Enter a number: "))
    operator = input("Enter an operator (+, -, *, /, ^, log) or 'q' to quit: ")
    num2 = float(input("Enter another number: "))
    
    calculate(num1, operator, num2)
            
main()