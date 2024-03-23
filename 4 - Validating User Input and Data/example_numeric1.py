import re

def validate_strictly_numeric(input_string):
  pattern = r"^\d+$"
  match = re.search(pattern, input_string)
  return match is not None

user_input = input("Enter a number: ")

if validate_strictly_numeric(user_input):
  print("Valid number!")
else:
  print("Invalid number.")
