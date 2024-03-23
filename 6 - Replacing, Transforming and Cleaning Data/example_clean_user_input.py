import re

def clean_phone_number(phone_number):
  digits_only = re.sub(r"\D", "", phone_number)
  if len(digits_only) != 10:
    return None
  
  formatted_number = f"({digits_only[:3]}) {digits_only[3:6]}-{digits_only[6:]}"
  return formatted_number

user_input = input("Enter your phone number: ")

cleaned_number = clean_phone_number(user_input)

if cleaned_number:
  print("Cleaned phone number:", cleaned_number)
else:
  print("Invalid phone number.")
