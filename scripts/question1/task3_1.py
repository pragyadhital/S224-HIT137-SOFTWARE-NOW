from collections import Counter
import string
import csv

def count_word_occurrences(file_path):
    
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator).lower()

   
    words = text.split()

    
    word_counts = Counter(words)

    return word_counts

def save_word_occurrences_to_csv(word_occurrences, output_csv_file):
    
    with open(output_csv_file, 'w', newline='', encoding='utf-8') as csv_file:
        
        csv_writer = csv.writer(csv_file)

       
        csv_writer.writerow(['Word', 'Occurrences'])

        
        for word, count in word_occurrences.items():
            csv_writer.writerow([word, count])

def save_top_n_occurrences_to_csv(word_occurrences, output_csv_file, top_n=10):
   
    sorted_occurrences = sorted(word_occurrences.items(), key=lambda x: x[1], reverse=True)

    
    top_n_occurrences = sorted_occurrences[:top_n]

    
    with open(output_csv_file, 'w', newline='', encoding='utf-8') as csv_file:
        
        csv_writer = csv.writer(csv_file)

        
        csv_writer.writerow(['Word', 'Occurrences'])

        
        for word, count in top_n_occurrences:
            csv_writer.writerow([word, count])

    print(f'Top {top_n} word occurrences saved to {output_csv_file}.')



text_file_path = r'F:\CDU\HIT137 SOFTWARE NOW\HIT137_Software Now_Assignment 2\outputs\output1.txt'


word_occurrences = count_word_occurrences(text_file_path)

output_csv_file = 'TOPword_occurrences.csv'



save_top_n_occurrences_to_csv(word_occurrences, output_csv_file, top_n=30)


for word, count in word_occurrences.items():
    print(f'{word}: {count} times')
