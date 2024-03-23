import re

text = "This is a sample text."
pattern = "sample"

match = re.search(pattern, text)

if match:
  print("Found a match!")
else:
  print("No match found.")
