import csv
import re

def clean_data(row):
  date_pattern = r"(\d{2})/(\d{2})/(\d{4})"
  row[0] = re.sub(date_pattern, r"\3-\1-\2", row[0])

  price_pattern = r"[^\d.]"
  row[1] = re.sub(price_pattern, "", row[1])
  return row


input_file = "input.csv"
output_file = "output.csv"

with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
  reader = csv.reader(infile)
  writer = csv.writer(outfile)

  header = next(reader)
  writer.writerow(header)

  for row in reader:
    cleaned_row = clean_data(row)
    writer.writerow(cleaned_row)
