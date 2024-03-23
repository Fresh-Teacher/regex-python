import re

pattern = r'hello'
text = 'Hello, world!'

match = re.search(pattern, text, re.IGNORECASE)

if match:
  print(f'Matched string: {match.group()}')
else:
  print(f'No match found')
