def decrypt(text, key):
    # Initialize an empty string to hold the decrypted text
    decrypted_text = ""
    
    # Loop through each character in the text
    for char in text:
        # Check if the character is a letter (ignores spaces, numbers, and symbols)
        if char.isalpha():
            # Get the ASCII code of the character and shift it by the key (Caesar Cipher decryption)
            shifted = ord(char) - key
            
            # Handle lowercase letters separately
            if char.islower():
                # If the shifted value is less than 'a', wrap around by adding 26 (for the alphabet length)
                if shifted < ord('a'):
                    shifted += 26
            
            # Handle uppercase letters separately
            elif char.isupper():
                # If the shifted value is less than 'A', wrap around by adding 26 (for the alphabet length)
                if shifted < ord('A'):
                    shifted += 26
            
            # Append the decrypted character to the result string
            decrypted_text += chr(shifted)
        
        else:
            # Non-alphabet characters (spaces, punctuation, etc.) are added unchanged
            decrypted_text += char
    
    # Return the fully decrypted text
    return decrypted_text

# Example encrypted text (using ROT13 encryption where each letter is shifted by 13 positions)
encrypted_text = """
tybony_inenvoyr = 100
zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}

qrs cebrff_ahzoref():
    tybony tybony_inenvoyr
    ybpny_inenvoyr = 5
    ahzoref = [1, 2, 3, 4, 5]

    juvyr ybpny_inenvoyr > 0:
        vs ybpny_inenvoyr % 2 == 0:
            ahzoref.erzbir(ybpny_inenvoyr)
        ybpny_inenvoyr -= 1

    erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny_inenvoyr = 10
    zl_qvpg['xrl4'] = ybpny_inenvoyr

zbqvsl_qvpg(5)

qrs hcangr_tybony():
    tybony tybony_inenvoyr
    tybony_inenvoyr += 10

sbe v va enatr(5):
    cevag(v)
    v += 1

vs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10:
    cevag("Pbaqvgvba zrg!")
vs 5 abg va zl_qvpg:
    cevag("5 abg sbeq va gur qvpgvbanel!")
cevag(tybony_inenvoyr)
cevag(zl_qvpg)
cevag(zl_frg)
"""

# Key for decryption (13 for ROT13, which shifts by 13 letters)
key = 13

# Decrypt the encrypted text using the key
decrypted_text = decrypt(encrypted_text, key)

# Print the decrypted text to the console
print(decrypted_text)
