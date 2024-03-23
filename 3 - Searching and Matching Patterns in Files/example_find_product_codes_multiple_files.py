import os
import re

def extract_product_codes(file_path, output_file):
  with open(file_path, 'r') as f:
    text = f.read()
    pattern = r'\b[A-Z]{2}\d{2}-[A-Z]{2}\d{2}\b|\b\d{3}-\d{3}\b'
    matches = re.findall(pattern, text)
    
    with open(output_file, 'w') as output_f:
      for match in matches:
        output_f.write(f'{match}\n')

file_pairs = [('file1.txt', 'codes1.txt'), ('file2.txt', 'codes2.txt'), ('file3.txt', 'codes3.txt')]

for input_file, output_file in file_pairs:
  input_path = os.path.join('input', input_file)
  output_path = os.path.join('output', output_file)
  extract_product_codes(input_path, output_path)
