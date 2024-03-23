import re

pattern = r'\b\w{4}\b' # match a word with exactly 4 letters
text = 'The quick brown fox jumps over the lazy dog'

new_text = re.sub(pattern, '****', text)
print(new_text)
