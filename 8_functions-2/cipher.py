"""
    This program encrypts and decrypts a string using a key, shifting each letter by the key.
"""
def cipher(mode: str, string: str, key: int) -> str:
    # encrpyts or decrypts a string using a key
    new_str = ""
    for char in string:

        if mode == "encrypt":
            if char.isupper(): # if char is uppercase
                new_str += chr((ord(char) + key - 65) % 26 + 65) # we shift the char by the key (in ASCII) and wrap around the alphabet
            elif char.islower(): # if char is lowercase
                new_str += chr((ord(char) + key - 97) % 26 + 97) 
            else: # if char is not a letter
                new_str += char # this is to keep the spaces and punctuation

        elif mode == "decrypt":
            if char.isupper():
                new_str += chr((ord(char) - key - 65) % 26 + 65)
            elif char.islower():
                new_str += chr((ord(char) - key - 97) % 26 + 97)
            else:
                new_str += char
                
    return new_str

"""
    Main function to run the program.
"""
def main():
    
    mode = input("Type 'encrypt' or 'decrypt': ")
    string = input("Enter a string: ")
    key = int(input("Enter a key (shift number): "))
    print(cipher(mode, string, key))
    
if __name__ == "__main__":
    main()