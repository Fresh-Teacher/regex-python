import re

with open("sample4.txt", "r") as f:
  text = f.read()
  
pattern = r"\b[A-Z]{2}\d{2}-[A-Z]{2}\d{2}\b|\b\d{3}-\d{3}\b"
matches = re.findall(pattern, text)

print("All product codes:", matches)
