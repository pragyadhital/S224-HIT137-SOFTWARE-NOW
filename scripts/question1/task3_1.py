import re
import csv
from collections import Counter

def count_word_occurrences(file_path):
    """
    Count the occurrences of words in a text file and return the top 30 words.
    
    Args:
        file_path (str): Path to the text file.
    
    Returns:
        dict: A dictionary of the top 30 most common words and their counts.
    """
    word_counts = Counter()
    
    # Read the text file and update word counts
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        
        # Use regex to find all words (alphanumeric and apostrophes only)
        words = re.findall(r'\b[a-zA-Z\']+\b', text)
        
        # Convert words to lowercase and update the counter
        word_counts.update(word.lower() for word in words)

    # Get the top 30 most common words as a dictionary
    return dict(word_counts.most_common(30))

def save_to_csv(data_dict, output_csv_file):
    """
    Save the dictionary of words and their counts to a CSV file.
    
    Args:
        data_dict (dict): A dictionary of words and their counts.
        output_csv_file (str): Path to the output CSV file.
    """
    with open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Write the header
        writer.writerow(['Word', 'Count'])
        
        # Write word-count pairs
        for word, count in data_dict.items():
            writer.writerow([word, count])

# Example Usage
if __name__ == "__main__":
    input_file = './output/final_csv.txt'  # Path to the text file
    output_csv = './output/top_30_common_words.csv'  # Path to save the CSV file
    
    # Count word occurrences and get the top 30 words
    top_30_words = count_word_occurrences(input_file)
    
    # Save the top 30 words and their counts to a CSV file
    save_to_csv(top_30_words, output_csv)
    
    print(f"Top 30 common words saved to {output_csv}")
