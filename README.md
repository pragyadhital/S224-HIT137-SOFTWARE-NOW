# Assignment 2: NLP and Python Programming Challenges

## Project Overview
Welcome to the collaborative repository for Assignment 2 of Software Now. This project includes a series of tasks focused on Natural Language Processing (NLP) and Python programming. Our team worked together to tackle challenges ranging from text processing to image manipulation, showcasing technical expertise and teamwork.

## Team Members
- **Pragya Dhital**
- **Dhiraj Chhetri**
- **Yubraj Regmi**
- **Subhash Shahu**

## Assignment Breakdown

### Question 1: Natural Language Processing with Python
This section focuses on applying NLP techniques using popular libraries such as SpaCy, scispaCy, and Transformers.

#### Task 1: Text Data Aggregation
- **Objective**: Combine text from multiple CSV files into a single `.txt` file for further analysis.

#### Task 2: Setting Up NLP Libraries
- **Tools Installed**:
  - **SpaCy**: Deployed with specialized models like `en_core_sci_sm` and `en_ner_bc5cdr_md` for processing biomedical text.
  - **Transformers (Hugging Face)**: Integrated BioBERT, a model designed for recognizing entities like diseases and drugs.

#### Task 3: Word Frequency and Tokenization
- **Task 3.1**: Used Python to perform word frequency analysis on the text file, identifying the top 30 most frequent words, which were saved to a CSV file.
- **Task 3.2**: Utilized the `AutoTokenizer` function from the Transformers library to create a function that identifies and ranks the top 30 unique tokens from the text.

#### Task 4: Named-Entity Recognition (NER) Comparison
- Conducted NER to extract `disease` and `drug` entities using both SpaCy and BioBERT models, then compared the results to evaluate the performance and differences between them.

### Question 2: The Quest for Hidden Knowledge
Embark on a programming journey through the mythical land of Pythoria, where code solves puzzles to unlock the path to hidden treasure.

#### Chapter 1: The Gatekeeper’s Challenge
- **Task**: Modify pixel values of the image `Chapter1.png` using an algorithmically generated number, producing a new image (`chapter1out.png`). The sum of all red pixel values in the new image is required to proceed to the next chapter.

#### Chapter 2: The Chamber of Strings
- Further exploration of this chapter will occur in later stages of the quest.

### Question 3: Decryption and Debugging
- This task required decrypting a provided code, identifying and fixing errors in the decrypted version, and explaining the corrections with detailed comments.

### Question 4: Collaborative GitHub Repository
- A public GitHub repository was created to track the team's progress, where all members actively contributed. This repository serves as both a codebase and a record of the team’s collective efforts.

## Repository Structure
- **`data/`**: Contains CSV files with raw text data.
- **`scripts/`**: Python scripts for running each task.
- **`output/`**: Contains the `.txt` file, CSV outputs, and processed images.
- **`images/`**: Original and processed images from Chapter 1.
- **`notebooks/`**: Jupyter notebooks for development and testing.
- **`README.md`**: Project documentation and overview.
- **`LICENSE`**: Licensing details for the repository.

## How to Use
1. **Environment Setup**: Install the required libraries by running `pip install -r requirements.txt`.
2. **Running Scripts**: The Scripts can be run from the HOMEDIR as we have made the script to run as module. 
```bash
# Running the Script 
python -m  scripts.question2.chapter1
```
3. **View Outputs**: All results are saved in the `output/` folder for review.

## Contribution Log
The repository reflects the collaborative work of all four team members, with GitHub commit logs ensuring transparency and tracking individual contributions.

## License
This project is licensed under the MIT License, promoting open collaboration and sharing.
