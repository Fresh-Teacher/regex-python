import re

file_extensions = ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx']

with open('sample2.txt', 'r') as f:
  text = f.read()
  pattern = r'\b\w+\.(?:' + '|'.join(file_extensions) + r')\b'
  matches = re.findall(pattern, text)

print(matches)
