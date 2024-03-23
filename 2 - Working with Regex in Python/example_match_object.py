import re

pattern = r'(\d{3})-(\d{3}-\d{4})' # match a phone number in the format XXX-XXX-XXXX
text = 'My phone number is 555-555-1234'

match = re.search(pattern, text)

if match:
  print(f'Matched phone number: {match.group()}')
  print(f'Area code: {match.group(1)}')
  print(f'Phone number: {match.group(2)}')
  print(f'Start position: {match.start()}')
  print(f'End position: {match.end()}')
  print(f'Span: {match.span()}')
