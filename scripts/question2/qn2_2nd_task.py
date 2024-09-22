## string separation

def separate_and_convert(s):
    number_string = ''.join(c for c in s if c.isdigit())
    letter_string = ''.join(c for c in s if c.isalpha())

    
    even_numbers = [int(num) for num in number_string if int(num) % 2 == 0]
    even_numbers_ascii = [ord(str(num)) for num in even_numbers]

    
    upper_case_letters = [char for char in letter_string if char.isupper()]
    upper_case_ascii = [ord(char) for char in upper_case_letters]

    return ''.join(map(str, even_numbers_ascii)), ''.join(map(str, upper_case_ascii))



input_string = '56аA1984sktr235270aYmn145ss785fsq31D0'
result_numbers, result_letters = separate_and_convert(input_string)

print("Number String:", result_numbers)
print("Letter String:", result_letters)
    



## cryptogram

def decrypt_cryptogram(cryptogram, shift):
    decrypted_text = ""
    for char in cryptogram:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

def find_shift_key(cryptogram):
    for shift in range(1, 26):
        decrypted_text = decrypt_cryptogram(cryptogram, shift)
        
        if any(word in decrypted_text.lower() for word in ['the', 'and', 'is', 'of']):
            return shift
    return None


cryptogram = "VZ FRYSFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZUXR ZVFGXRF V NZ BHG BS PBAGEBY NAONG GVZRF UNEQ GB UNAQYR CHG VS LEH PNAG UNAQYR ZR NG ZL JBEFG GURA LEH FHER NE URVYGGAG QRFREIR ZR NG ZL ORFG ZNEVLA ZBAEBR"
shift_key = find_shift_key(cryptogram)

if shift_key is not None:
    decrypted_text = decrypt_cryptogram(cryptogram, shift_key)
    print(f"Shift Key (s): {shift_key}")
    print("Decrypted Quote:", decrypted_text)
else:
    print("Shift key not found.")




