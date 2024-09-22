import spacy
from spacy import displacy
from spacy.tokens import DocBin
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch
from collections import Counter

def ner_spacy(text, model_name):
    nlp = spacy.load(model_name)
    doc = nlp(text)
    return doc

def ner_biobert(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=2)
    
    
    tokens = tokenizer.convert_ids_to_tokens(predictions[0].tolist())
    
    return tokens

def compare_ner_results(text, spacy_model_name, biobert_model_name):
    
    spacy_doc = ner_spacy(text, spacy_model_name)

    
    tokenizer_biobert = AutoTokenizer.from_pretrained(biobert_model_name)
    model_biobert = AutoModelForTokenClassification.from_pretrained(biobert_model_name)

    
    tokens_biobert = ner_biobert(text, tokenizer_biobert, model_biobert)

    
    entities_spacy = [ent.text for ent in spacy_doc.ents]

    
    entities_biobert = [token for token in tokens_biobert if token.startswith("B-")]

    
    common_entities = set(entities_spacy) & set(entities_biobert)
    unique_entities_spacy = set(entities_spacy) - set(entities_biobert)
    unique_entities_biobert = set(entities_biobert) - set(entities_spacy)

    
    print(f"Total entities detected by spaCy: {len(entities_spacy)}")
    print(f"Total entities detected by BioBERT: {len(entities_biobert)}")
    print(f"Common entities: {len(common_entities)}")
    print(f"Entities unique to spaCy: {len(unique_entities_spacy)}")
    print(f"Entities unique to BioBERT: {len(unique_entities_biobert)}")

    
    print("\nMost common words for spaCy:")
    counter_spacy = Counter(entities_spacy)
    for word, count in counter_spacy.most_common(10):
        print(f"{word}: {count}")

    
    print("\nMost common words for BioBERT:")
    counter_biobert = Counter(entities_biobert)
    for word, count in counter_biobert.most_common(10):
        print(f"{word}: {count}")

    
    displacy.serve(spacy_doc, style="ent")


file_path = r'F:\CDU\HIT137 SOFTWARE NOW\HIT137_Software Now_Assignment 2\outputs\output1.txt' 

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

spacy_model_name = 'en_core_sci_sm'  
biobert_model_name = 'dmis-lab/biobert-base-cased-v1.1'  
compare_ner_results(text, spacy_model_name, biobert_model_name)
