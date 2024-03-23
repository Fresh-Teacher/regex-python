import re

def validate_numeric(input_string):
  pattern = r"^-?\d+(\.\d+)?$"
  match = re.search(pattern, input_string)
  return match is not None

user_input = input("Enter a number to validate (negative and decimal numbers allowed): ")

if validate_numeric(user_input):
  print("Valid input!")
else:
  print("Invalid input.")

