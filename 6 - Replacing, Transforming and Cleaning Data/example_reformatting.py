import re

def reformat_dates(text):
    pattern = r"(?<=Date: )\d{2}/\d{2}/\d{4}"
    return re.sub(pattern, lambda m: m.group(0)[6:] + '-' + m.group(0)[:5], text)

def reformat_prices(text):
    pattern = r"(?<=Price: )\$\d{1,3}(?:,\d{3})*"
    return re.sub(pattern, lambda m: m.group(0).replace(',', ''), text)

with open("invoice.txt", "r") as f:
    content = f.read()

content = reformat_dates(content)
content = reformat_prices(content)

with open("reformatted_invoice.txt", "w") as f:
    f.write(content)

print("Dates and prices reformatted!")
