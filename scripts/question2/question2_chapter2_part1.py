def process_string(s):
    # Extract all digits from the input string and join them into a single string
    number_str = ''.join([ch for ch in s if ch.isdigit()])
    
    # Extract all alphabetic characters from the input string and join them into a single string
    letter_str = ''.join([ch for ch in s if ch.isalpha()])

    # Finding all even numbers from the extracted digits and converting them to integers
    even_numbers = [int(ch) for ch in number_str if int(ch) % 2 == 0]
    
    # Converting the even numbers to their ASCII values
    even_ascii = [ord(str(num)) for num in even_numbers]

    # Finding all uppercase letters from the extracted alphabetic characters
    uppercase_letters = [ch for ch in letter_str if ch.isupper()]
    
    # Converting the uppercase letters to their ASCII values
    uppercase_ascii = [ord(ch) for ch in uppercase_letters]

    # Print the extracted number string and letter string
    print(f"Number String: {number_str} and Letter String: {letter_str}")
    
    # Print the list of even numbers
    print(f"Even numbers: {even_numbers}")
    
    # Print the ASCII values of the even numbers
    print(f"Even numbers in ASCII: {even_ascii}")
    
    # Print the list of uppercase letters
    print(f"Uppercase letters: {uppercase_letters}")
    
    # Print the ASCII values of the uppercase letters
    print(f"Uppercase letters in ASCII: {uppercase_ascii}")


# Get the input string from the user
scenario_string = input("Please Enter your string: ")

# Process the input string using the defined function
process_string(scenario_string)
