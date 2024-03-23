import re

pattern = r'hello.*world'
text = 'hello\nworld'

match = re.search(pattern, text, re.DOTALL)

if match:
  print(f'Matched string: {match.group()}')
else:
  print(f'No match found')
