from transformers import BertTokenizer, BertForTokenClassification
import torch

# Load BioBERT tokenizer and model for token classification
tokenizer = BertTokenizer.from_pretrained('monologg/biobert_v1.1_pubmed', do_lower_case=False)
# Load BioBERT model with 2 labels (assuming labels for 'DISEASE' and 'DRUG')
model = BertForTokenClassification.from_pretrained('monologg/biobert_v1.1_pubmed', num_labels=2)

# Print the token labels used in the model (converts token ids to their respective tokens)
print(tokenizer.convert_ids_to_tokens(range(model.config.num_labels)))

# Function to extract entities (disease and drug) from the input text
def extract_entities(text):
    # Tokenize the input text and convert it to tensors for model input
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    
    # Get model predictions for the input tokens
    outputs = model(**inputs)
    
    # Get the predicted label (0 or 1) for each token, corresponding to 'DRUG' or 'DISEASE'
    predictions = torch.argmax(outputs.logits, dim=2)

    # List to hold identified entities
    entities = []

    # Map token predictions to their respective labels
    for token, prediction in zip(inputs["input_ids"][0], predictions[0]):
        # Convert token IDs back to strings
        token_str = tokenizer.convert_ids_to_tokens(token.item())
        
        # Determine the label based on the prediction (1 = 'DISEASE', 0 = 'DRUG', or 'O' for other)
        label = 'DISEASE' if torch.eq(prediction, torch.tensor(1)) else 'DRUG' if torch.eq(prediction, torch.tensor(0)) else 'O'
        
        # If the label is not 'O', append the token and label as a tuple to the entities list
        if label != 'O':
            entities.append((token_str, label))

    return entities  # Return the list of identified entities

# Process the text file
file_path = '/all_csv_file.txt'  # Path to the input text file

# Open and read the entire content of the file
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()  # Read the file contents into a string
    entities = extract_entities(text)  # Extract entities from the text

# Separate the extracted entities into 'diseases' and 'drugs'
diseases = [entity[0] for entity in entities if entity[1] == 'DISEASE']  # Extract disease entities
drugs = [entity[0] for entity in entities if entity[1] == 'DRUG']  # Extract drug entities

# Print the extracted diseases and drugs
print("Diseases:", diseases)
print("Drugs:", drugs)
