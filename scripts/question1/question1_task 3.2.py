from transformers import AutoTokenizer
from collections import Counter
from concurrent.futures import ProcessPoolExecutor

# Function to tokenize a chunk of text and count the token occurrences
def tokenize_and_count(chunk, model_name):
    # Load the tokenizer from the pre-trained model (e.g., BERT tokenizer)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # Tokenize the input chunk: encode it to token IDs, then decode it back to text, and finally tokenize it
    tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(chunk)))
    
    # Return a Counter object to count the frequency of each token in the chunk
    return Counter(tokens)

# Function to read a file in chunks (useful for processing large files)
def read_file_in_chunks(file_path, chunk_size=10 * 1024 * 1024):  # Default chunk size = 10 MB
    # Open the file in read mode with UTF-8 encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            # Read a chunk of the file based on the specified chunk size
            data_chunk = file.read(chunk_size)
            
            # If no more data is available, stop reading
            if not data_chunk:
                break
            
            # Yield the current chunk for processing
            yield data_chunk

# Function to process the file in parallel, tokenize, and display the most common tokens
def process_and_display_top_tokens(file_path, model_name, top_n=30, num_processes=2):
    # Check if the script is being run as the main process (necessary for multiprocessing)
    if __name__ == '__main__':
        # Use ProcessPoolExecutor to parallelize the task of tokenizing and counting
        with ProcessPoolExecutor(max_workers=num_processes) as executor:
            # Process each chunk of the file in parallel across multiple processes
            # `executor.map` applies `tokenize_and_count` to each chunk of text
            counters = list(executor.map(tokenize_and_count, read_file_in_chunks(file_path), [model_name] * num_processes))

        # Sum all the individual counters to get the total token frequencies
        total_counter = sum(counters, Counter())

        # Get the top N most common tokens from the aggregated counter
        top_tokens = total_counter.most_common(top_n)
        
        # Print the top tokens and their respective counts
        print(f"Top {top_n} tokens:")
        for token, count in top_tokens:
            print(f"{token}: {count}")

# Example usage:
file_path = 'aggregated_texts.txt'  # Path to the text file to process
model_name = 'bert-base-uncased'    # Pre-trained tokenizer model from the transformers library

# Call the function to process the file and display the top tokens
process_and_display_top_tokens(file_path, model_name)
