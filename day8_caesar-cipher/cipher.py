# code a cipher that takes a string and a key and a mode and returns a string

def cipher(mode: str, string: str, key: int) -> str:
    """Encrypts a string using a key"""
    new_str = ""
    for char in string:
        if mode == "encrypt":
            if char.isupper():
                new_str += chr((ord(char) + key - 65) % 26 + 65)
            elif char.islower():
                new_str += chr((ord(char) + key - 97) % 26 + 97)
            else:
                new_str += char
        elif mode == "decrypt":
            if char.isupper():
                new_str += chr((ord(char) - key - 65) % 26 + 65)
            elif char.islower():
                new_str += chr((ord(char) - key - 97) % 26 + 97)
            else:
                new_str += char
    return new_str

def main():
    """Main function"""
    mode = input("Enter a mode (encrypt, decrypt): ")
    string = input("Enter a string: ")
    key = int(input("Enter a key: "))
    print(cipher(mode, string, key))
    
if __name__ == "__main__":
    main()