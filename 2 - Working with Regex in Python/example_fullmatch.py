import re

pattern = r'\d{4}-\d{2}-\d{2}' # match a date string in the format yyyy-mm-dd
date_string = '2023-03-11'

match = re.fullmatch(pattern, date_string)

if match:
  print(f'The date string {date_string} is valid')
else:
  print(f'The date string {date_string} is not valid')
