from typing import Tuple

def get_nums_and_chars(s: str) -> Tuple[str, str]:
    """
    Extracts all numeric characters and all alphabetic letters from a string 
    and returns them as two separate strings in a tuple.

    Args:
        s (str): Input string.

    Returns:
        Tuple[str, str]: A tuple containing two strings:
                         - The first string with all numeric characters.
                         - The second string with all alphabetic characters.
    """
    # Extract all numeric characters
    all_numbers = ''.join(ch for ch in s if ch.isdigit())

    # Extract all alphabetic letters
    all_letters = ''.join(ch for ch in s if ch.isalpha())

    return all_numbers, all_letters

def get_ascii_value(c: str) -> int:
    """
    Returns the ASCII value of the given character.

    Args: 
        c (str): Single character input.

    Returns: 
        int: The ASCII value of the character.
    """
    return ord(c)

def process_numbers(num_str: str) -> str:
    """
    Converts even numbers in the input string to their ASCII values.

    Args:
        num_str (str): String containing numbers.

    Returns:
        str: A string where even numbers are converted to their ASCII values.
    """
    result = []
    for char in num_str:
        if int(char) % 2 == 0:
            result.append(str(get_ascii_value(char)))  # Convert even numbers to ASCII
        else:
            result.append(char)  # Leave odd numbers as they are
    return "".join(result)

def process_letters(letters_str: str) -> str:
    """
    Converts uppercase letters in the input string to their ASCII values.

    Args:
        letters_str (str): String containing letters.

    Returns:
        str: A string where uppercase letters are converted to their ASCII values.
    """
    result = []
    for char in letters_str:
        if char.isupper():
            result.append(str(get_ascii_value(char)))  # Convert uppercase letters to ASCII
        else:
            result.append(char)  # Leave lowercase letters as they are
    return "".join(result)

if __name__ == "__main__":
    s = "S6aAww1984sktr23527øaymn145ss785fsq31Dø"
    
    # Separate numbers and letters
    nums, letters = get_nums_and_chars(s)
    
    # Process numbers and letters
    result_nums = process_numbers(nums)
    result_letters = process_letters(letters)
    
    print(f"Processed Numbers: {result_nums}")
    print(f"Processed Letters: {result_letters}")
