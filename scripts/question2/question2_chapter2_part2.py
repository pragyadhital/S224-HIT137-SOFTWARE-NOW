def decipher_text(cipher_text, shift):
    result = []  # List to store the decrypted characters

    # Iterate through each character in the ciphered text
    for ch in cipher_text:
        if ch.isalpha():  # Check if the character is a letter (ignores punctuation/space)
            # Determine if the letter is uppercase or lowercase and set the base ASCII value
            shift_start = ord('A') if ch.isupper() else ord('a')
            
            # Shift the character back by the specified amount, wrapping around using modulo 26
            decrypted_char = chr((ord(ch) - shift_start - shift) % 26 + shift_start)
            result.append(decrypted_char)  # Add the decrypted character to the result list
        else:
            result.append(ch)  # If not a letter, keep the character unchanged (e.g., punctuation)

    # Combine the list of characters into a single string and return it
    return ''.join(result)

# Get input from the user for the ciphered text and the shift value
cipher_text = input("Enter your ciphered quote: ")
shift = int(input("Enter your shift value: "))

# Decrypt the message using the decipher_text function
decrypted_message = decipher_text(cipher_text, shift)

# Print the original (decrypted) message
print(f"If ciphered quote is '{cipher_text}' and Shift: {shift},\nthen the original quote is: {decrypted_message}")

