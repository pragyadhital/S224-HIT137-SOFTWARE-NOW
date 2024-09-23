# Assignment 2: NLP and Python Programming Challenges

## Project Overview
Welcome to our collaborative repository for the second assignment in [Course Name]. This project encompasses a series of intricate tasks focusing on Natural Language Processing (NLP) and Python programming. Our team has diligently worked together to tackle challenges ranging from text processing to image manipulation, demonstrating both technical prowess and collaborative synergy.

## Team Members
- **Ayush Dutta**
- **Angel Prajapati**
- **Tirtha Raj Pokhrel**
- **Sarita Lakai**

## Assignment Breakdown

### Question 1: Natural Language Processing with Python
This segment of the assignment is dedicated to the application of NLP techniques using powerful libraries such as SpaCy, scispaCy, and Transformers.

#### Task 1: Aggregating Text Data
- Objective: Consolidate the text content from multiple CSV files into a single `.txt` file for subsequent analysis.

#### Task 2: Library Setup
- Tools Installed:
  - **SpaCy**: Deployed with specialized models `en_core_sci_sm` and `en_ner_bc5cdr_md` for biomedical text processing.
  - **Transformers (Hugging Face)**: Integrated with BioBERT, a model adept at recognizing entities such as drugs and diseases.

#### Task 3: Word Frequency Analysis and Tokenization
- **Task 3.1**: We utilized a Python library to calculate word frequencies in the text file, isolating the top 30 most frequent words and exporting this data into a CSV file.
- **Task 3.2**: Leveraging the `AutoTokenizer` function from the Transformers library, we created a function to identify and rank the top 30 unique tokens from the text.

#### Task 4: Named-Entity Recognition (NER) Comparison
- We performed NER to extract `disease` and `drug` entities using both SpaCy models and BioBERT. The results were compared to analyze the efficacy and differences between these models.

### Question 2: The Quest for Hidden Knowledge
Embark on a code-driven adventure through the mystical land of Pythoria, where programming skills unlock the path to the hidden treasure.

#### Chapter 1: The Gatekeeper’s Challenge
- Task: Modify the pixel values of `Chapter1.png` using an algorithmically generated number and produce a new image (`chapter1out.png`). Sum all red pixel values from the new image to progress to the next chapter.

#### Chapter 2: The Chamber of Strings
- To be explored in subsequent stages of the quest.

### Question 3: Decoding and Debugging
- This task involved decrypting an encrypted code, identifying errors in the original decrypted code, and rectifying them with detailed explanations provided through comments.

### Question 4: Collaborative GitHub Repository
- A public GitHub repository has been created for this project, where all team members actively contributed. This repository not only serves as a codebase but also as a record of our collective efforts.

## Repository Structure
- **`data/`**: CSV files containing the raw text data.
- **`scripts/`**: Python scripts for executing each task.
- **`output/`**: Contains the `.txt` file, CSV output, and processed images.
- **`images/`**: The original and processed images from Chapter 1.
- **`notebooks/`**: Jupyter notebooks for development and testing.
- **`README.md`**: Project documentation and overview.
- **`LICENSE`**: Repository licensing information.

## How to Use
1. **Environment Setup**: Ensure all required libraries are installed by running `pip install -r requirements.txt`.
2. **Running Scripts**: Navigate to the `scripts/` directory and execute the scripts in sequential order.
3. **Review Outputs**: All results will be saved in the `output/` directory for easy access.

## Contribution Log
This repository highlights the collaborative efforts of all four team members, with contributions tracked via GitHub commits to ensure transparency and teamwork.

## License
The content of this repository is licensed under the MIT License, promoting open collaboration and sharing.


