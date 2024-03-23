import re

def validate_username(username):
  pattern = r"^[a-zA-Z]+[\w]*$"
  
  match = re.fullmatch(pattern, username)
  return match is not None

user_input = input("Enter a username: ")

if validate_username(user_input):
  print("Valid username!")
else:
  print("Invalid username.")
