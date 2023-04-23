# code a cipher that takes a string and a key and a mode and returns a string

def cipher(str: str, key: int, mode: str) -> str:
    """Encrypts or decrypts a string using a key and a mode"""
    if mode == "encrypt":
        return encrypt(str, key)
    elif mode == "decrypt":
        return decrypt(str, key)
    else:
        return "Invalid mode"
    
def encrypt(str: str, key: int) -> str:
    """Encrypts a string using a key"""
    encrypted = ""
    for char in str:
        encrypted += chr(ord(char) + key)
    return encrypted

def decrypt(str: str, key: int) -> str:
    """Decrypts a string using a key"""
    decrypted = ""
    for char in str:
        decrypted += chr(ord(char) - key)
    return decrypted

def main():
    """Main function"""
    mode = input("Enter a mode (encrypt, decrypt): ")
    str = input("Enter a string: ")
    key = int(input("Enter a key: "))
    print(cipher(str, key, mode))
    
if __name__ == "__main__":
    main()