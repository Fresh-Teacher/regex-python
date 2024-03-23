import re

pattern = r'\s+' # match one or more whitespace characters
text = 'The quick brown fox jumps over the lazy dog'

words = re.split(pattern, text, 3)
print(words)
