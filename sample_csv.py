import sys
import csv
import random

def sample_csv(input_file, output_file, sample_rate=0.1):
    # Read the input CSV
    with open(input_file, 'r') as infile:
        # Read all lines
        reader = csv.reader(infile)
        
        # Read the header
        header = next(reader)
        
        # Get all data rows
        rows = list(reader)
    
    # Calculate number of rows to sample
    sample_size = max(1, int(len(rows) * sample_rate))
    
    # Randomly sample rows
    sampled_rows = random.sample(rows, sample_size)
    
    # Write sampled rows to output file
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        
        # Write header
        writer.writerow(header)
        
        # Write sampled rows
        writer.writerows(sampled_rows)
    
    print(f"Sampled {sample_size} rows out of {len(rows)} total rows")

def main():
    # Check if correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python sample_csv.py <input_file> <output_file>")
        sys.exit(1)
    
    # Get input and output file names
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Sample the CSV
    sample_csv(input_file, output_file)

if __name__ == "__main__":
    main()