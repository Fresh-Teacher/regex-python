import re

pattern = r'The' # match the word "The" at the beginning of a string
text = 'The quick brown fox'

match = re.match(pattern, text)

if match:
  print(f'The text string starts with the word "The"')
else:
  print(f'The text string does not start with the word "The"')
