import re

pattern = r'\d+' # match one or more digits
text = 'The price of the book is $19.99 and the price of the movie is $12.50'

matches = re.findall(pattern, text)
print(matches)
