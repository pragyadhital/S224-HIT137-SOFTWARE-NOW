import csv
from collections import Counter
import re

def get_most_common_words(input_file, output_file, num_top_words=30):
    # Opening and reading the contents of the input text file
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Cleaning and normalizing the text by removing non-alphabetic characters
    # and converting all text to lowercase
    content = re.sub(r'[^a-zA-Z\s]', '', content)  # Keep only letters and spaces
    words_list = content.lower().split()  # Split the text into a list of words

    # Counting occurrences of each word in the list
    word_frequency = Counter(words_list)

    # Retrieving the most frequent words (default is top 30 words)
    most_common_words = word_frequency.most_common(num_top_words)

    # Writing the top words and their frequencies to a CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Word', 'Count'])  # Write the header row

        # Write each word and its count into the CSV file
        for word, count in most_common_words:
            writer.writerow([word, count])

# Input and output file paths
input_file = 'aggregated_texts.txt'
output_file = 'top_words.csv'

# Call the function to process the input file and generate the output CSV
get_most_common_words(input_file, output_file)
