import re

pattern = r'\d+$'
text = 'Line 1\nLine 2\nLine 3'

matches = re.findall(pattern, text)

print(matches)
