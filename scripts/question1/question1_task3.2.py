from transformers import AutoTokenizer
from collections import Counter
import heapq
from concurrent.futures import ThreadPoolExecutor
import re

# Initialize AutoTokenizer (you can replace 'bert-base-uncased' with your tokenizer model)
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

def process_chunk(chunk):
    # Tokenize the chunk
    tokens = tokenizer.tokenize(chunk)
    # Filter out non-alphabetic tokens
    filtered_tokens = [token for token in tokens if token.isalpha()]
    # Return token counts as a Counter object
    return Counter(filtered_tokens)

def get_top_n_words(token_counts, n=30):
    # Use heapq to get top n most frequent words
    return heapq.nlargest(n, token_counts.items(), key=lambda x: x[1])

def process_large_file_concurrent(file_path, chunk_size=1024*1024, max_workers=4):
    token_counts = Counter()  # Dictionary to hold word counts

    with open(file_path, 'r', encoding='utf-8') as file:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            while True:
                chunk = file.read(chunk_size)  # Read file in chunks
                if not chunk:
                    break
                # Submit chunk processing to the thread pool
                futures.append(executor.submit(process_chunk, chunk))

            # Collect results as they complete
            for future in futures:
                token_counts.update(future.result())  # Merge the results

    return token_counts

# Example Usage
if __name__ == "__main__":
    # Path to your large text file
    file_path = './output/final_csv.txt'

    # Process the file and get word counts using concurrency
    token_counts = process_large_file_concurrent(file_path)

    # Get the top 30 most frequent words
    top_30_words = get_top_n_words(token_counts, n=30)

    # Print the top 30 words and their counts
    for word, count in top_30_words:
        print(f"{word}: {count}")
