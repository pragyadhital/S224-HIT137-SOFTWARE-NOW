
def encrypt(text, key):

    # Normalize the key 
    key = key % 26

    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text
    
# Using decrypt function to find the encrypted key 

def decrypt(encrypted_text, key):  
    key = key%26
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

# Example usage:
encryted_text = """VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY
NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF
URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"""


key = 0

if __name__ == "__main__": 
    with open('scripts/question3/code.txt', 'r') as f: 
        encryted_code = f.read() 
    print(decrypt(encryted_code, 13 ))

    # print(decrypt(encryted_text, 13))
    # key is 13 
    # for key in range(1,26): 
    #     print(f"Trying Encryption Key {key}")
    #     output = decrypt(encryped_code, key)
    #     print(f"Output is {output}") 
    #     print("*"*50)
# Encrypt the original code
# encrypted_code = encrypt(original_code, key)
# print("Encrypted Code:", encrypted_code)

# # Decrypt the encrypted code
# decrypted_code = decrypt(encrypted_code, key)
# print("Decrypted Code:", decrypted_code)
