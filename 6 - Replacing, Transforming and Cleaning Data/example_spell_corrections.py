import re

def replace_misspellings(text, corrections):
  for misspelled, correct in corrections.items():
    pattern = re.compile(rf"\b{misspelled}\b", re.IGNORECASE)
    text = pattern.sub(correct, text)
  return text


corrections = {
  "recieve": "receive",
  "adress": "address",
  "acomodate": "accommodate"
}

with open("document.txt", "r") as f:
  content = f.read()

corrected_content = replace_misspellings(content, corrections)

with open("corrected_document.txt", "w") as f:
  f.write(corrected_content)
print("Misspellings corrected!")
