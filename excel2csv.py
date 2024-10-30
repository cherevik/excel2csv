import pandas as pd
import csv
import argparse
import os

def clean_excel_to_csv(input_file, output_file):
    df = pd.read_excel(input_file, dtype=str)  
    df = df.apply(lambda col: col.map(lambda x: x.strip() if isinstance(x, str) else x))
    df.to_csv(output_file, index=False, quoting=csv.QUOTE_MINIMAL)
    print(f"CSV export completed: {output_file}")

parser = argparse.ArgumentParser(description="Convert an Excel file to a trimmed CSV file.")
parser.add_argument("input_file", type=str, help="Path to the input Excel file.")
parser.add_argument("output_file", type=str, help="Path to the output CSV file.")

args = parser.parse_args()

if not os.path.exists(args.input_file):
    print(f"Error: The input file '{args.input_file}' does not exist.")
else:
    clean_excel_to_csv(args.input_file, args.output_file)
