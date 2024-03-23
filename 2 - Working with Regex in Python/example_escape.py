import re

pattern = r'.' # match any char
text = 'The quick brown fox.'

escaped_pattern = re.escape(pattern)
print("new pattern: ", escaped_pattern)
match = re.search(escaped_pattern, text)

if match:
  print(f'Found a dot in the text')
else:
  print(f'Could not find dot in the text')
