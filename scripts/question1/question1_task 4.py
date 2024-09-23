import spacy  # Importing spaCy library for natural language processing
from spacy import displacy  # Importing displacy for visualizing named entities
from spacy.tokens import DocBin  # Importing DocBin for efficient storage of large doc objects
from transformers import AutoTokenizer, AutoModelForTokenClassification  # Importing transformer models
import torch  # PyTorch for tensor operations and model handling
from collections import Counter  # Counter to count occurrences of entities

# Function to perform Named Entity Recognition (NER) using spaCy
def ner_spacy(text, model_name):
    nlp = spacy.load(model_name)  # Load the spaCy model
    doc = nlp(text)  # Process the text to get a doc object with entities
    return doc  # Return the processed doc

# Function to perform NER using a pre-trained BioBERT model
def ner_biobert(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors="pt")  # Tokenize the text and return it in PyTorch format
    outputs = model(**inputs)  # Perform token classification
    predictions = torch.argmax(outputs.logits, dim=2)  # Get the most likely token classes (argmax)

    # Convert predicted token IDs back to tokens
    tokens = tokenizer.convert_ids_to_tokens(predictions[0].tolist())
    
    return tokens  # Return the list of tokens with their predicted classes

# Function to compare the results of spaCy and BioBERT NER
def compare_ner_results(text, spacy_model_name, biobert_model_name):
    
    # Perform NER using spaCy
    spacy_doc = ner_spacy(text, spacy_model_name)

    # Load the BioBERT tokenizer and model
    tokenizer_biobert = AutoTokenizer.from_pretrained(biobert_model_name)
    model_biobert = AutoModelForTokenClassification.from_pretrained(biobert_model_name)

    # Perform NER using BioBERT
    tokens_biobert = ner_biobert(text, tokenizer_biobert, model_biobert)

    # Extract named entities from spaCy
    entities_spacy = [ent.text for ent in spacy_doc.ents]

    # Extract named entities from BioBERT (assuming 'B-' indicates the start of an entity)
    entities_biobert = [token for token in tokens_biobert if token.startswith("B-")]

    # Compare the entities found by both models
    common_entities = set(entities_spacy) & set(entities_biobert)  # Entities found by both
    unique_entities_spacy = set(entities_spacy) - set(entities_biobert)  # Entities unique to spaCy
    unique_entities_biobert = set(entities_biobert) - set(entities_spacy)  # Entities unique to BioBERT

    # Print statistics of the comparison
    print(f"Total entities detected by spaCy: {len(entities_spacy)}")
    print(f"Total entities detected by BioBERT: {len(entities_biobert)}")
    print(f"Common entities: {len(common_entities)}")
    print(f"Entities unique to spaCy: {len(unique_entities_spacy)}")
    print(f"Entities unique to BioBERT: {len(unique_entities_biobert)}")

    # Print the most common entities for spaCy
    print("\nMost common words for spaCy:")
    counter_spacy = Counter(entities_spacy)
    for word, count in counter_spacy.most_common(10):
        print(f"{word}: {count}")

    # Print the most common entities for BioBERT
    print("\nMost common words for BioBERT:")
    counter_biobert = Counter(entities_biobert)
    for word, count in counter_biobert.most_common(10):
        print(f"{word}: {count}")

    # Visualize the named entities detected by spaCy using displaCy
    displacy.serve(spacy_doc, style="ent")

# File path to the text file containing the input text
file_path = r'F:\CDU\HIT137 SOFTWARE NOW\HIT137_Software Now_Assignment 2\outputs\output1.txt' 

# Read the input text from the file
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Define the spaCy and BioBERT models to use
spacy_model_name = 'en_core_sci_sm'  # spaCy model specialized for scientific texts
biobert_model_name = 'dmis-lab/biobert-base-cased-v1.1'  # BioBERT model pre-trained for biomedical text

# Compare the NER results between spaCy and BioBERT
compare_ner_results(text, spacy_model_name, biobert_model_name)
