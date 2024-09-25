import spacy
from concurrent.futures import ThreadPoolExecutor

# Load the spaCy model
nlp = spacy.load("en_core_sci_sm")  # Load a spaCy model for scientific texts
nlp.disable_pipes('parser', 'ner')  # Disable unnecessary components (parser, NER) to speed up processing

# Function to process a batch of text within a chunk
def process_batch(chunk):
    docs = nlp.pipe(chunk, disable=["parser", "ner"])  # Process the text chunks using the spaCy model
    
    # Lists to hold disease and drug entities
    diseases = []
    drugs = []

    # Iterate through the processed documents and extract entities
    for doc in docs:
        # Append text of entities labeled "DISEASE" to the diseases list
        diseases.extend([ent.text for ent in doc.ents if ent.label_ == "DISEASE"])
        # Append text of entities labeled "CHEMICAL" to the drugs list
        drugs.extend([ent.text for ent in doc.ents if ent.label_ == "CHEMICAL"])

    # Return both lists of extracted entities
    return diseases, drugs

# Function to process a large text file in batches
def process_large_text_file(file_path, chunk_size=10 * 1024 * 1024, batch_size=10):
    # Open the file in read mode with UTF-8 encoding
    with open(file_path, "r", encoding="utf-8") as file:
        chunks = []  # List to hold chunks of text
        
        while True:
            # Read a chunk of the file based on the specified chunk size
            chunk = file.read(chunk_size)
            if not chunk:
                break  # End the loop when there's no more data to read
            chunks.append(chunk)  # Append the chunk to the list
            
            # If the chunk list reaches the batch size, yield it for processing
            if len(chunks) == batch_size:
                yield chunks
                chunks = []  # Clear the chunk list after yielding

        # Yield any remaining chunks if they exist after the loop
        if chunks:
            yield chunks

# Process each batch of chunks concurrently
def process_batches(batches):
    # Use ThreadPoolExecutor to process batches concurrently
    with ThreadPoolExecutor() as executor:
        # Map the process_batch function to each batch and gather the results
        results = list(executor.map(process_batch, batches))

    # Aggregate diseases and drugs from all results
    all_diseases = [disease for result in results for disease in result[0]]
    all_drugs = [drug for result in results for drug in result[1]]

    # Print the extracted diseases and drugs
    print("Diseases:", all_diseases)
    print("Drugs:", all_drugs)

    return all_diseases, all_drugs  # Return the aggregated lists of entities

# Example usage:
file_path = '../aggregated_texts.txt'  # Path to the input text file
chunk_size = 100000  # Size of each chunk to read from the file (100 KB)
batch_size = 10  # Number of chunks to process at once
batches = process_large_text_file(file_path, chunk_size=chunk_size, batch_size=batch_size)  # Get the batches of text

# Process the batches and extract entities
process_batches(batches)
