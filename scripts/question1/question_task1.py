import pandas as pd

# A list of the text columns of each CSV file name
csv_files = [('CSV1.csv', 'SHORT-TEXT'), ('CSV2.csv', 'TEXT'), ('CSV3.csv','TEXT'), ('CSV4.csv','TEXT')]

# List to hold text data from every file
all_texts1 = []

# Examine every CSV file to extract text data.
for (file1, text_column1) in csv_files:
    # A CSV file is read into a DataFrame.
    df = pd.read_csv(file1)

    # Considering that the column with text data is called "text"
    if text_column1 in df.columns:
        # Take text data and add it to the list.
        all_texts1.extend(df[text_column1].astype(str).tolist())

# Adding textual data to a fresh text document.
output_file = 'all_csv_file.txt'
with open(output_file, 'w', encoding='utf-8') as f:
    for text in all_texts1:
        f.write(text + '\n')

print(f'Text information written to {output_file}')
