import re

phone_pattern = r'\d{3}-\d{3}-\d{4}'
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
zip_pattern = r'\b\d{5}(?:-\d{4})?\b'
order_pattern = r'\b[A-Z]{2}-\d{4}-\d{4}\b'
hex_pattern = r'#[A-Fa-f0-9]{6}'

with open('sample3.txt', 'r') as f:
  text = f.read()
  phone_match = re.search(phone_pattern, text)
  email_match = re.search(email_pattern, text)
  zip_match = re.search(zip_pattern, text)
  order_match = re.search(order_pattern, text)
  hex_match = re.search(hex_pattern, text)

if phone_match:
  print(f'Phone number found: {phone_match.group()}')
if email_match:
  print(f'Email address found: {email_match.group()}')
if zip_match:
  print(f'Zip code found: {zip_match.group()}')
if order_match:
  print(f'Order number found: {order_match.group()}')
if hex_match:
  print(f'Hex color code found: {hex_match.group()}')
