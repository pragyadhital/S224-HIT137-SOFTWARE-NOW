import spacy
from concurrent.futures import ThreadPoolExecutor
from transformers import BertTokenizer, BertForTokenClassification
import torch
from collections import Counter

# Load SpaCy model for scientific texts
nlp_spacy = spacy.load("en_core_sci_sm")

# Load BioBERT model and tokenizer
tokenizer_biobert = BertTokenizer.from_pretrained('monologg/biobert_v1.1_pubmed', do_lower_case=False)
model_biobert = BertForTokenClassification.from_pretrained('monologg/biobert_v1.1_pubmed')

# Disable unneeded pipelines for efficiency
nlp_spacy.disable_pipes('parser', 'ner')

# Function to process a batch of text with SpaCy
def process_spacy_batch(chunk):
    docs = nlp_spacy.pipe(chunk, disable=["parser", "ner"])
    
    # Extract disease and drug entities
    diseases = []
    drugs = []

    for doc in docs:
        diseases.extend([ent.text for ent in doc.ents if ent.label_ == "DISEASE"])
        drugs.extend([ent.text for ent in doc.ents if ent.label_ == "CHEMICAL"])

    return diseases, drugs

# Function to process large text files in batches
def process_large_text_file(file_path, chunk_size=10 * 1024 * 1024, batch_size=10):
    with open(file_path, "r", encoding="utf-8") as file:
        # Read the file in chunks
        chunks = []
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break  # End of file
            chunks.append(chunk)
            if len(chunks) == batch_size:
                yield chunks
                chunks = []

        # Yield the remaining chunks
        if chunks:
            yield chunks

# Process batches of text concurrently
def process_batches(batches):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(process_spacy_batch, batches))

    # Aggregate results
    all_diseases = [disease for result in results for disease in result[0]]
    all_drugs = [drug for result in results for drug in result[1]]

    # Print the extracted diseases and drugs
    print("SpaCy Diseases:", Counter(all_diseases))
    print("SpaCy Drugs:", Counter(all_drugs))

    return all_diseases, all_drugs

# Extract entities using BioBERT
def extract_entities_biobert(text):
    inputs = tokenizer_biobert(text, return_tensors="pt", truncation=True)
    outputs = model_biobert(**inputs)
    predictions = torch.argmax(outputs.logits, dim=2)

    # Map token predictions to entities
    entities = []
    for token, prediction in zip(inputs["input_ids"][0], predictions[0]):
        token_str = tokenizer_biobert.convert_ids_to_tokens(token.item())
        label = 'DISEASE' if torch.eq(prediction, torch.tensor(1)) else 'DRUG' if torch.eq(prediction, torch.tensor(0)) else 'O'
        
        if label != 'O':
            entities.append((token_str, label))

    return entities

# Process the text file
file_path = './output/final_csv.txt'  # Update with your file path
chunk_size = 100000  # Adjust as needed
batch_size = 10
batches = process_large_text_file(file_path, chunk_size=chunk_size, batch_size=batch_size)

# Process batches with SpaCy
spacy_diseases, spacy_drugs = process_batches(batches)

# Read the whole text for BioBERT processing
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()
    biobert_entities = extract_entities_biobert(text)

# Separate BioBERT entities
biobert_diseases = [entity[0] for entity in biobert_entities if entity[1] == 'DISEASE']
biobert_drugs = [entity[0] for entity in biobert_entities if entity[1] == 'DRUG']

# Print the results from BioBERT
print("BioBERT Diseases:", Counter(biobert_diseases))
print("BioBERT Drugs:", Counter(biobert_drugs))

# Compare entities from both methods
common_diseases = set(spacy_diseases).intersection(biobert_diseases)
unique_spacy_diseases = set(spacy_diseases).difference(biobert_diseases)
unique_biobert_diseases = set(biobert_diseases).difference(spacy_diseases)

common_drugs = set(spacy_drugs).intersection(biobert_drugs)
unique_spacy_drugs = set(spacy_drugs).difference(biobert_drugs)
unique_biobert_drugs = set(biobert_drugs).difference(spacy_drugs)

print("\nCommon Diseases between SpaCy and BioBERT:", common_diseases)
print("Unique to SpaCy Diseases:", unique_spacy_diseases)
print("Unique to BioBERT Diseases:", unique_biobert_diseases)

print("\nCommon Drugs between SpaCy and BioBERT:", common_drugs)
print("Unique to SpaCy Drugs:", unique_spacy_drugs)
print("Unique to BioBERT Drugs:", unique_biobert_drugs)
