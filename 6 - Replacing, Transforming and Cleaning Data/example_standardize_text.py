import re

text = "The quick, brown fox jumps over the lazy dog!"

no_punctuation = re.sub(r"[^\w\s]", "", text)
print("Text without punctuation:", no_punctuation)

lowercase_text = no_punctuation.lower()
print("Lowercase text:", lowercase_text)

words = re.split(r"\s+", lowercase_text)
print("Tokenized words:", words)
