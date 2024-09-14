import os

def merge_csv_files(input_dir, output_file):
    """
    Merges all CSV files from the specified input directory into a single output file.
    
    Args:
        input_dir (str): Directory containing the CSV files.
        output_file (str): Path to the final merged CSV file.
    """
    try:
        # Ensure the input directory exists
        if not os.path.exists(input_dir):
            raise FileNotFoundError(f"The directory {input_dir} does not exist.")
        
        # List all CSV files in the input directory
        csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

        if not csv_files:
            raise FileNotFoundError("No CSV files found in the specified directory.")

        # Open the output file in write mode
        with open(output_file, 'w') as resultfile_fp:
            # Iterate through each CSV file
            for file_name in csv_files:
                full_file_path = os.path.join(input_dir, file_name)
                
                # Open each CSV file in read mode
                with open(full_file_path, 'r') as csvfile_fp:
                    # Read the content and write to the result file
                    resultfile_fp.write(csvfile_fp.read())
                    resultfile_fp.write('\n')  # Add a newline between files

        print(f"Successfully merged {len(csv_files)} files into {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_directory = "data"
    output_file = "output/final_csv.txt"
    merge_csv_files(input_directory, output_file)
